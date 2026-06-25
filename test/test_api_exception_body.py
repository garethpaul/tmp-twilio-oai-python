import pytest

from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import ApiException


def client_that_raises(exception):
    client = ApiClient(Configuration())

    def raise_exception(*args, **kwargs):
        raise exception

    client.request = raise_exception
    return client


def test_api_exception_without_body_is_preserved():
    exception = ApiException(status=500, reason="server error")
    client = client_that_raises(exception)

    with pytest.raises(ApiException) as raised:
        client.call_api("/2010-04-01/Accounts.json", "GET")

    assert raised.value is exception
    assert raised.value.body is None


def test_api_exception_with_string_body_is_preserved():
    exception = ApiException(status=400, reason="bad request")
    exception.body = "already decoded"
    client = client_that_raises(exception)

    with pytest.raises(ApiException) as raised:
        client.call_api("/2010-04-01/Accounts.json", "GET")

    assert raised.value is exception
    assert raised.value.body == "already decoded"


def test_api_exception_with_bytes_body_is_decoded():
    exception = ApiException(status=400, reason="bad request")
    exception.body = b'{"message":"bad request"}'
    client = client_that_raises(exception)

    with pytest.raises(ApiException) as raised:
        client.call_api("/2010-04-01/Accounts.json", "GET")

    assert raised.value is exception
    assert raised.value.body == '{"message":"bad request"}'


def test_api_exception_bytes_honor_declared_response_charset():
    exception = ApiException(status=400, reason="bad request")
    exception.body = b'{"message":"caf\xe9"}'
    exception.headers = {"Content-Type": "application/json; charset=iso-8859-1"}
    client = client_that_raises(exception)

    with pytest.raises(ApiException) as raised:
        client.call_api("/2010-04-01/Accounts.json", "GET")

    assert raised.value is exception
    assert raised.value.body == '{"message":"café"}'


def test_api_exception_unknown_charset_falls_back_to_utf8_replacement():
    exception = ApiException(status=400, reason="bad request")
    exception.body = b'{"message":"bad \xff"}'
    exception.headers = {"content-type": "text/plain; charset=x-unknown"}
    client = client_that_raises(exception)

    with pytest.raises(ApiException) as raised:
        client.call_api("/2010-04-01/Accounts.json", "GET")

    assert raised.value.body == '{"message":"bad �"}'
