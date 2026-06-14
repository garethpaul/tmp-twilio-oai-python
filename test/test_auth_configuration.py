import base64

import pytest

from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration


class DummyResponse:
    status = 200
    data = b""

    def getheader(self, name, default=None):
        return default

    def getheaders(self):
        return {}


def test_basic_auth_not_sent_without_runtime_credentials():
    client = ApiClient(Configuration())
    headers = {}
    query_params = []

    client.update_params_for_auth(
        headers,
        query_params,
        ["accountSid_authToken"],
        "/2010-04-01/Accounts.json",
        "GET",
        None,
    )

    assert "Authorization" not in headers
    assert query_params == []


def test_basic_auth_not_sent_with_blank_runtime_credentials():
    for configuration in (
        Configuration(username="", password="secret"),
        Configuration(username="AC123", password=""),
        Configuration(username="", password=""),
        Configuration(username="   ", password="secret"),
        Configuration(username="AC123", password="   "),
        Configuration(username="   ", password="   "),
    ):
        client = ApiClient(configuration)
        headers = {}
        query_params = []

        client.update_params_for_auth(
            headers,
            query_params,
            ["accountSid_authToken"],
            "/2010-04-01/Accounts.json",
            "GET",
            None,
        )

        assert configuration.get_basic_auth_token() is None
        assert "Authorization" not in headers
        assert query_params == []


def test_basic_auth_header_uses_runtime_credentials():
    client = ApiClient(Configuration(username="AC123", password="secret"))
    headers = {}
    query_params = []

    client.update_params_for_auth(
        headers,
        query_params,
        ["accountSid_authToken"],
        "/2010-04-01/Accounts.json",
        "GET",
        None,
    )

    expected = base64.b64encode(b"AC123:secret").decode("ascii")
    assert headers["Authorization"] == "Basic %s" % expected
    assert query_params == []


def test_basic_auth_header_trims_runtime_credentials():
    client = ApiClient(Configuration(username="  AC123  ", password="  secret  "))
    headers = {}
    query_params = []

    client.update_params_for_auth(
        headers,
        query_params,
        ["accountSid_authToken"],
        "/2010-04-01/Accounts.json",
        "GET",
        None,
    )

    expected = base64.b64encode(b"AC123:secret").decode("ascii")
    assert headers["Authorization"] == "Basic %s" % expected
    assert query_params == []


def test_basic_auth_header_not_sent_to_non_local_http_host():
    client = ApiClient(
        Configuration(
            host="http://api.example.test",
            username="AC123",
            password="secret",
        )
    )
    headers = {}
    query_params = []

    client.update_params_for_auth(
        headers,
        query_params,
        ["accountSid_authToken"],
        "/2010-04-01/Accounts.json",
        "GET",
        None,
    )

    assert "Authorization" not in headers
    assert query_params == []


def test_basic_auth_header_allowed_for_local_http_host():
    client = ApiClient(
        Configuration(
            host="http://localhost:8080",
            username="AC123",
            password="secret",
        )
    )
    headers = {}
    query_params = []

    client.update_params_for_auth(
        headers,
        query_params,
        ["accountSid_authToken"],
        "/2010-04-01/Accounts.json",
        "GET",
        None,
    )

    expected = base64.b64encode(b"AC123:secret").decode("ascii")
    assert headers["Authorization"] == "Basic %s" % expected
    assert query_params == []


@pytest.mark.parametrize(
    "request_host, expect_authorization",
    [
        ("https://api.example.test", True),
        ("http://localhost:8080", True),
        ("http://api.example.test", False),
        ("ftp://localhost", False),
    ],
)
def test_basic_auth_uses_effective_request_host(
    request_host,
    expect_authorization,
):
    client = ApiClient(
        Configuration(
            username="AC123",
            password="secret",
        )
    )
    captured = {}

    def capture_request(method, url, headers=None, **kwargs):
        captured["url"] = url
        captured["headers"] = headers
        return DummyResponse()

    client.request = capture_request
    client.call_api(
        "/2010-04-01/Accounts.json",
        "GET",
        auth_settings=["accountSid_authToken"],
        _host=request_host,
        _return_http_data_only=True,
    )

    assert captured["url"] == request_host + "/2010-04-01/Accounts.json"
    assert ("Authorization" in captured["headers"]) is expect_authorization


def test_https_override_can_authorize_when_default_host_is_disallowed():
    configuration = Configuration(
        host="http://api.example.test",
        username="AC123",
        password="secret",
    )
    client = ApiClient(configuration)
    captured = {}

    def capture_request(method, url, headers=None, **kwargs):
        captured["url"] = url
        captured["headers"] = headers
        return DummyResponse()

    client.request = capture_request
    client.call_api(
        "/2010-04-01/Accounts.json",
        "GET",
        auth_settings=["accountSid_authToken"],
        _host="https://api.example.test",
        _return_http_data_only=True,
    )

    expected = base64.b64encode(b"AC123:secret").decode("ascii")
    assert captured["url"] == "https://api.example.test/2010-04-01/Accounts.json"
    assert captured["headers"]["Authorization"] == "Basic %s" % expected


def test_basic_auth_replaces_case_insensitive_operation_authorization():
    configuration = Configuration(
        host="https://api.example.test",
        username="AC123",
        password="secret",
    )
    client = ApiClient(configuration)
    operation_headers = {
        "authorization": "Basic caller-value",
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
        "GET",
        header_params=operation_headers,
        auth_settings=["accountSid_authToken"],
        _return_http_data_only=True,
    )

    expected = base64.b64encode(b"AC123:secret").decode("ascii")
    assert captured["headers"]["Authorization"] == "Basic %s" % expected
    assert "authorization" not in captured["headers"]
    assert captured["headers"]["X-Operation"] == "operation-value"
    assert operation_headers == original_headers


def test_cookie_auth_replaces_case_insensitive_existing_cookie():
    configuration = Configuration()
    configuration.auth_settings = lambda: {
        "session": {
            "type": "api_key",
            "in": "cookie",
            "key": "Cookie",
            "value": "session=generated",
        }
    }
    client = ApiClient(configuration)
    headers = {"cookie": "session=caller", "X-Operation": "operation-value"}

    client.update_params_for_auth(
        headers,
        [],
        ["session"],
        "/2010-04-01/Accounts.json",
        "GET",
        None,
        request_host="https://api.example.test",
    )

    assert headers == {
        "Cookie": "session=generated",
        "X-Operation": "operation-value",
    }
