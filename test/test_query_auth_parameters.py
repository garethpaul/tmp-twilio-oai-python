from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration


class DummyResponse:
    status = 200
    data = b""

    def getheader(self, name, default=None):
        return default

    def getheaders(self):
        return {}


def test_query_auth_initializes_missing_query_params():
    configuration = Configuration()
    configuration.auth_settings = lambda: {
        "query_token": {
            "type": "apiKey",
            "in": "query",
            "key": "AuthToken",
            "value": "secret",
        }
    }
    client = ApiClient(configuration)
    captured = {}

    def capture_request(method, url, query_params=None, **kwargs):
        captured["query_params"] = query_params
        return DummyResponse()

    client.request = capture_request

    client.call_api(
        "/2010-04-01/Accounts.json",
        "GET",
        auth_settings=["query_token"],
        _return_http_data_only=True,
    )

    assert captured["query_params"] == [("AuthToken", "secret")]
