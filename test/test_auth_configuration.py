import base64

from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration


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
