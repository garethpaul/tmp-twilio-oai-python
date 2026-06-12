import logging

import pytest

from openapi_client.configuration import Configuration
from openapi_client.exceptions import UnauthorizedException
from openapi_client.rest import RESTClientObject


class DummyHTTPResponse:
    reason = "OK"

    def __init__(self, status, data):
        self.status = status
        self.data = data

    def getheaders(self):
        return {}

    def getheader(self, name, default=None):
        return default


class ResponsePoolManager:
    def __init__(self, response):
        self.response = response

    def request(self, method, url, **kwargs):
        return self.response


def client_with_response(status, data):
    client = RESTClientObject(Configuration())
    client.pool_manager = ResponsePoolManager(DummyHTTPResponse(status, data))
    return client


def test_success_response_logs_metadata_without_body(caplog):
    body = b'{"auth_token":"super-secret"}'
    client = client_with_response(200, body)
    caplog.set_level(logging.DEBUG, logger="openapi_client.rest")

    response = client.request(
        "GET", "https://api.twilio.com/2010-04-01/Accounts.json"
    )

    assert response.data == body
    assert caplog.messages == [
        f"response received: status=200 bytes={len(body)}"
    ]
    assert "super-secret" not in caplog.text


def test_error_response_logs_metadata_without_body(caplog):
    body = b'{"message":"invalid auth token: super-secret"}'
    client = client_with_response(401, body)
    caplog.set_level(logging.DEBUG, logger="openapi_client.rest")

    with pytest.raises(UnauthorizedException) as captured:
        client.request("GET", "https://api.twilio.com/2010-04-01/Accounts.json")

    assert captured.value.body == body
    assert caplog.messages == [
        f"response received: status=401 bytes={len(body)}"
    ]
    assert "super-secret" not in caplog.text
