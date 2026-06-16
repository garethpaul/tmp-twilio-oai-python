import pytest

from openapi_client.configuration import Configuration
from openapi_client.exceptions import ApiValueError
from openapi_client.rest import RESTClientObject


class DummyHTTPResponse:
    status = 200
    reason = "OK"
    data = b""

    def __init__(self):
        self.read_offset = 0

    def getheaders(self):
        return {}

    def getheader(self, name, default=None):
        return default

    def read(self, amt=None, decode_content=None):
        if amt is None:
            chunk = self.data[self.read_offset:]
        else:
            chunk = self.data[self.read_offset:self.read_offset + amt]
        self.read_offset += len(chunk)
        return chunk

    def release_conn(self):
        pass

    def close(self):
        pass


class CapturingPoolManager:
    def __init__(self):
        self.calls = []

    def request(self, method, url, **kwargs):
        self.calls.append(
            {
                "method": method,
                "url": url,
                "headers": dict(kwargs.get("headers") or {}),
                "body": kwargs.get("body"),
                "fields": kwargs.get("fields"),
                "encode_multipart": kwargs.get("encode_multipart"),
            }
        )
        return DummyHTTPResponse()


def client_with_capturing_pool():
    client = RESTClientObject(Configuration())
    client.pool_manager = CapturingPoolManager()
    return client


def test_request_does_not_mutate_headers_when_defaulting_content_type():
    client = client_with_capturing_pool()
    headers = {"X-Test": "1"}

    client.request("GET", "https://api.twilio.com", headers=headers)

    assert headers == {"X-Test": "1"}
    assert client.pool_manager.calls[0]["headers"] == {
        "X-Test": "1",
        "Content-Type": "application/json",
    }


def test_request_does_not_mutate_headers_for_multipart_uploads():
    client = client_with_capturing_pool()
    headers = {"Content-Type": "multipart/form-data"}

    client.request(
        "POST",
        "https://api.twilio.com",
        headers=headers,
        post_params=[("media", "body")],
    )

    assert headers == {"Content-Type": "multipart/form-data"}
    assert "Content-Type" not in client.pool_manager.calls[0]["headers"]


def test_parameterized_json_content_type_uses_json_body_without_duplicate_header():
    client = client_with_capturing_pool()
    headers = {"content-type": "Application/Problem+JSON; charset=utf-8"}

    client.request(
        "POST",
        "https://api.twilio.com",
        headers=headers,
        body={"message": "hello"},
    )

    call = client.pool_manager.calls[0]
    assert headers == {"content-type": "Application/Problem+JSON; charset=utf-8"}
    assert call["headers"] == headers
    assert call["body"] == '{"message": "hello"}'


def test_lowercase_parameterized_form_content_type_uses_form_fields():
    client = client_with_capturing_pool()
    headers = {
        "content-type": "Application/X-WWW-Form-Urlencoded; charset=utf-8"
    }

    client.request(
        "POST",
        "https://api.twilio.com",
        headers=headers,
        post_params=[("Body", "hello")],
    )

    call = client.pool_manager.calls[0]
    assert call["headers"] == headers
    assert call["fields"] == [("Body", "hello")]
    assert call["encode_multipart"] is False


def test_lowercase_parameterized_multipart_header_is_removed_from_copy():
    client = client_with_capturing_pool()
    headers = {"content-type": "Multipart/Form-Data; boundary=caller-value"}

    client.request(
        "POST",
        "https://api.twilio.com",
        headers=headers,
        post_params=[("media", "body")],
    )

    call = client.pool_manager.calls[0]
    assert headers == {"content-type": "Multipart/Form-Data; boundary=caller-value"}
    assert call["headers"] == {}
    assert call["fields"] == [("media", "body")]
    assert call["encode_multipart"] is True


def test_duplicate_content_type_case_variants_fail_before_transport():
    client = client_with_capturing_pool()

    with pytest.raises(ApiValueError, match="multiple Content-Type"):
        client.request(
            "POST",
            "https://api.twilio.com",
            headers={
                "Content-Type": "application/json",
                "content-type": "application/x-www-form-urlencoded",
            },
            body={"message": "hello"},
        )

    assert client.pool_manager.calls == []


def test_write_request_appends_query_params_to_existing_query_string():
    client = client_with_capturing_pool()

    client.request(
        "POST",
        "https://api.twilio.com/2010-04-01/Messages.json?Page=1",
        headers={"Content-Type": "application/json"},
        query_params=[("PageSize", "50")],
    )

    assert (
        client.pool_manager.calls[0]["url"]
        == "https://api.twilio.com/2010-04-01/Messages.json?Page=1&PageSize=50"
    )


def test_write_request_appends_repeated_query_params():
    client = client_with_capturing_pool()

    client.request(
        "POST",
        "https://api.twilio.com/2010-04-01/Messages.json",
        headers={"Content-Type": "application/json"},
        query_params=[("Status", ["queued", "sent"])],
    )

    assert (
        client.pool_manager.calls[0]["url"]
        == "https://api.twilio.com/2010-04-01/Messages.json?Status=queued&Status=sent"
    )


def test_request_rejects_unsupported_method_before_pool_request():
    client = client_with_capturing_pool()

    with pytest.raises(ApiValueError, match="Unsupported HTTP method: TRACE"):
        client.request("TRACE", "https://api.twilio.com/2010-04-01/Messages.json")

    assert client.pool_manager.calls == []
