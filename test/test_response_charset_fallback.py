from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration


class DummyResponse:
    status = 200

    def __init__(self, data, content_type):
        self.data = data
        self.content_type = content_type

    def getheader(self, name, default=None):
        if name.lower() == "content-type":
            return self.content_type
        return default

    def getheaders(self):
        return {"content-type": self.content_type}


def decoded_response(data, content_type):
    client = ApiClient(Configuration())
    response = DummyResponse(data, content_type)
    client.request = lambda *args, **kwargs: response
    client.call_api(
        "/2010-04-01/Accounts.json",
        "GET",
        response_type=None,
        auth_settings=[],
        _return_http_data_only=False,
    )
    return client.last_response.data


def test_honors_valid_declared_response_charset():
    assert decoded_response(b"caf\xe9", "text/plain; charset=iso-8859-1") == "café"


def test_replaces_malformed_bytes_for_declared_charset():
    assert decoded_response(b"bad \xff", "application/json; charset=utf-8") == "bad �"


def test_unknown_response_charset_falls_back_to_utf8_replacement():
    assert decoded_response(b"hello \xff", "text/plain; charset=x-unknown") == "hello �"


def test_binary_and_streaming_responses_skip_text_decoding():
    binary = b"\xff\x00"
    client = ApiClient(Configuration())
    response = DummyResponse(binary, "application/octet-stream; charset=x-unknown")
    client.request = lambda *args, **kwargs: response
    client.deserialize = lambda response_data, *args, **kwargs: response_data.data

    client.call_api(
        "/binary",
        "GET",
        response_type="bytes",
        auth_settings=[],
        _return_http_data_only=False,
    )
    assert client.last_response.data == binary

    streaming = DummyResponse(binary, "text/plain; charset=x-unknown")
    client.request = lambda *args, **kwargs: streaming
    assert client.call_api(
        "/stream",
        "GET",
        auth_settings=[],
        _preload_content=False,
    ) is streaming
    assert streaming.data == binary
