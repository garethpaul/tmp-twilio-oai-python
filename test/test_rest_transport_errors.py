import pytest
import urllib3

from openapi_client.configuration import Configuration
from openapi_client.exceptions import ApiException
from openapi_client.rest import RESTClientObject


class FailingPoolManager:
    def __init__(self, error):
        self.error = error

    def request(self, method, url, **kwargs):
        raise self.error


def test_request_wraps_read_timeout_as_api_exception():
    url = "https://api.twilio.com/2010-04-01/Accounts.json"
    timeout = urllib3.exceptions.ReadTimeoutError(None, url, "timed out")
    client = RESTClientObject(Configuration())
    client.pool_manager = FailingPoolManager(timeout)

    with pytest.raises(ApiException) as captured:
        client.request("GET", url)

    assert captured.value.status == 0
    assert "ReadTimeoutError" in captured.value.reason
    assert captured.value.__cause__ is timeout
