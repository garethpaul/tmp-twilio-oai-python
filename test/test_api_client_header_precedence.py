from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration


class DummyResponse:
    status = 200
    data = b""

    def getheader(self, name, default=None):
        return default

    def getheaders(self):
        return {}


def test_operation_headers_override_defaults_without_mutating_input():
    client = ApiClient(Configuration())
    client.set_default_header("Content-Type", "application/json")
    client.set_default_header("X-Default", "default-value")
    operation_headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Operation": "operation-value",
    }
    original_headers = dict(operation_headers)
    captured = {}

    def capture_request(method, url, headers=None, **kwargs):
        captured["headers"] = headers
        return DummyResponse()

    client.request = capture_request
    client.call_api(
        "/2010-04-01/Accounts.json",
        "POST",
        header_params=operation_headers,
        _return_http_data_only=True,
    )

    assert captured["headers"]["Content-Type"] == "application/x-www-form-urlencoded"
    assert captured["headers"]["X-Default"] == "default-value"
    assert captured["headers"]["X-Operation"] == "operation-value"
    assert operation_headers == original_headers


def test_operation_headers_override_case_insensitive_defaults():
    client = ApiClient(Configuration(), cookie="session=client")
    client.set_default_header("Authorization", "Basic default")
    client.set_default_header("Content-Type", "application/json")
    client.set_default_header("X-Default", "default-value")
    original_defaults = dict(client.default_headers)
    operation_headers = {
        "Authorization": "Basic superseded operation",
        "authorization": "Basic operation",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "session=operation",
    }
    original_headers = dict(operation_headers)
    captured = {}

    def capture_request(method, url, headers=None, **kwargs):
        captured["headers"] = headers
        return DummyResponse()

    client.request = capture_request
    client.call_api(
        "/2010-04-01/Accounts.json",
        "POST",
        header_params=operation_headers,
        _return_http_data_only=True,
    )

    assert captured["headers"]["authorization"] == "Basic operation"
    assert captured["headers"]["content-type"] == "application/x-www-form-urlencoded"
    assert "Authorization" not in captured["headers"]
    assert "Content-Type" not in captured["headers"]
    assert captured["headers"]["Cookie"] == "session=client"
    assert "cookie" not in captured["headers"]
    assert captured["headers"]["X-Default"] == "default-value"
    assert operation_headers == original_headers
    assert client.default_headers == original_defaults
