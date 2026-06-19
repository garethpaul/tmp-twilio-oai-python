import gzip
import io

import pytest
import urllib3

from openapi_client.configuration import Configuration
from openapi_client.exceptions import ApiException, ApiValueError, UnauthorizedException
from openapi_client.rest import RESTClientObject


class BoundedHTTPResponse:
    reason = "OK"

    def __init__(
        self,
        data=b"",
        status=200,
        content_length=None,
        content_encoding=None,
        read_error=None,
    ):
        self.status = status
        self.data = data
        self.content_length = content_length
        self.content_encoding = content_encoding
        self.read_error = read_error
        self.read_calls = []
        self.read_offset = 0
        self.closed = False
        self.released = False

    def getheaders(self):
        return {}

    def getheader(self, name, default=None):
        if name.lower() == "content-length" and self.content_length is not None:
            return self.content_length
        if name.lower() == "content-encoding" and self.content_encoding is not None:
            return self.content_encoding
        return default

    def read(self, amt=None, decode_content=None):
        self.read_calls.append((amt, decode_content))
        if self.read_error is not None:
            raise self.read_error
        if amt is None:
            chunk = self.data[self.read_offset:]
        else:
            chunk = self.data[self.read_offset:self.read_offset + amt]
        self.read_offset += len(chunk)
        return chunk

    def release_conn(self):
        self.released = True

    def close(self):
        self.closed = True


class ResponsePoolManager:
    def __init__(self, response):
        self.response = response
        self.calls = []

    def request(self, method, url, **kwargs):
        self.calls.append(kwargs)
        return self.response


def client_with_response(response, limit=8):
    configuration = Configuration()
    configuration.max_response_body_size = limit
    client = RESTClientObject(configuration)
    client.pool_manager = ResponsePoolManager(response)
    return client


def test_configuration_defaults_to_five_mebibyte_response_limit():
    assert Configuration().max_response_body_size == 5 * 1024 * 1024


@pytest.mark.parametrize("value", [None, True, False, 0, -1, 1.5, "8"])
def test_client_rejects_invalid_response_body_limits(value):
    configuration = Configuration()
    configuration.max_response_body_size = value

    with pytest.raises(ApiValueError, match="positive integer"):
        RESTClientObject(configuration)


def test_preloaded_response_accepts_exact_limit_and_releases_connection():
    transport_response = BoundedHTTPResponse(data=b"12345678")
    client = client_with_response(transport_response)

    response = client.request("GET", "https://api.twilio.com")

    assert response.data == b"12345678"
    assert client.pool_manager.calls[0]["preload_content"] is False
    assert transport_response.read_calls == [(9, True), (1, True)]
    assert transport_response.released is True
    assert transport_response.closed is False


def test_declared_oversize_response_closes_without_reading():
    transport_response = BoundedHTTPResponse(
        data=b"small",
        content_length="9",
    )
    client = client_with_response(transport_response)

    with pytest.raises(ApiException, match="exceeds the configured 8-byte limit"):
        client.request("GET", "https://api.twilio.com")

    assert transport_response.read_calls == []
    assert transport_response.closed is True
    assert transport_response.released is False


def test_head_response_ignores_representation_content_length():
    transport_response = BoundedHTTPResponse(content_length="9")
    client = client_with_response(transport_response)

    response = client.request("HEAD", "https://api.twilio.com")

    assert response.data == b""
    assert transport_response.released is True
    assert transport_response.closed is False


def test_decoded_oversize_response_closes_without_returning_body():
    transport_response = BoundedHTTPResponse(data=b"123456789")
    client = client_with_response(transport_response)

    with pytest.raises(ApiException) as captured:
        client.request("GET", "https://api.twilio.com")

    assert captured.value.status == 200
    assert captured.value.body is None
    assert transport_response.read_calls == [(9, True)]
    assert transport_response.closed is True
    assert transport_response.released is False


def test_compressed_response_is_limited_by_decoded_size():
    transport_response = urllib3.response.HTTPResponse(
        body=io.BytesIO(gzip.compress(b"123456789")),
        headers={"Content-Encoding": "gzip"},
        status=200,
        preload_content=False,
        decode_content=True,
    )
    client = client_with_response(transport_response)

    with pytest.raises(ApiException):
        client.request("GET", "https://api.twilio.com")

    assert transport_response.closed is True


def test_compressed_content_length_does_not_override_decoded_limit():
    body = b"12345678"
    encoded_body = gzip.compress(body)
    transport_response = urllib3.response.HTTPResponse(
        body=io.BytesIO(encoded_body),
        headers={
            "Content-Encoding": "gzip",
            "Content-Length": str(len(encoded_body)),
        },
        status=200,
        preload_content=False,
        decode_content=True,
    )
    client = client_with_response(transport_response)

    response = client.request("GET", "https://api.twilio.com")

    assert response.data == body


def test_error_response_preserves_bounded_body_and_status_exception():
    transport_response = BoundedHTTPResponse(data=b"denied", status=401)
    client = client_with_response(transport_response)

    with pytest.raises(UnauthorizedException) as captured:
        client.request("GET", "https://api.twilio.com")

    assert captured.value.body == b"denied"
    assert transport_response.released is True
    assert transport_response.closed is False


def test_streaming_response_remains_caller_managed():
    transport_response = BoundedHTTPResponse(data=b"123456789")
    client = client_with_response(transport_response)

    response = client.request(
        "GET",
        "https://api.twilio.com",
        _preload_content=False,
    )

    assert response is transport_response
    assert client.pool_manager.calls[0]["preload_content"] is False
    assert transport_response.read_calls == []
    assert transport_response.released is False
    assert transport_response.closed is False


def test_streaming_error_response_is_closed_before_exception():
    transport_response = BoundedHTTPResponse(data=b"denied", status=401)
    client = client_with_response(transport_response)

    with pytest.raises(UnauthorizedException):
        client.request(
            "GET",
            "https://api.twilio.com",
            _preload_content=False,
        )

    assert transport_response.read_calls == []
    assert transport_response.released is False
    assert transport_response.closed is True


def test_preload_failure_closes_response_and_preserves_cause():
    transport_error = urllib3.exceptions.ProtocolError("truncated response")
    transport_response = BoundedHTTPResponse(read_error=transport_error)
    client = client_with_response(transport_response)

    with pytest.raises(ApiException) as captured:
        client.request("GET", "https://api.twilio.com")

    assert captured.value.__cause__ is transport_error
    assert transport_response.closed is True
    assert transport_response.released is False
