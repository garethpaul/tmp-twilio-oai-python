from openapi_client.configuration import Configuration
from openapi_client.rest import RESTClientObject


class DummyHTTPResponse:
    status = 200
    reason = "OK"
    data = b""

    def getheaders(self):
        return {}

    def getheader(self, name, default=None):
        return default


class CapturingPoolManager:
    def __init__(self):
        self.calls = []

    def request(self, method, url, **kwargs):
        self.calls.append(
            {
                "method": method,
                "url": url,
                "headers": dict(kwargs.get("headers") or {}),
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
