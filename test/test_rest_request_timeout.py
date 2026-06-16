import math

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
        self.calls.append(kwargs)
        return DummyHTTPResponse()


def client_with_capturing_pool():
    client = RESTClientObject(Configuration())
    client.pool_manager = CapturingPoolManager()
    return client


def test_request_accepts_positive_total_timeout():
    client = client_with_capturing_pool()

    client.request("GET", "https://api.twilio.com", _request_timeout=2.5)

    timeout = client.pool_manager.calls[0]["timeout"]
    assert timeout.total == 2.5


def test_request_preserves_default_timeout_when_omitted():
    client = client_with_capturing_pool()

    client.request("GET", "https://api.twilio.com")

    assert client.pool_manager.calls[0]["timeout"] is None


@pytest.mark.parametrize(
    ("value", "expected_connect", "expected_read"),
    [
        ((1, 2), 1, 2),
        ((None, 2), None, 2),
        ((1, None), 1, None),
        ((None, None), None, None),
    ],
)
def test_request_accepts_connect_read_timeout_tuple(
    value,
    expected_connect,
    expected_read,
):
    client = client_with_capturing_pool()

    client.request(
        "GET",
        "https://api.twilio.com",
        _request_timeout=value,
    )

    timeout = client.pool_manager.calls[0]["timeout"]
    assert timeout.connect_timeout == expected_connect
    assert timeout.read_timeout == expected_read


@pytest.mark.parametrize(
    "value",
    [
        True,
        "5",
        [],
        [1, 2],
        (),
        (1,),
        (1, 2, 3),
        0,
        -1,
        math.nan,
        math.inf,
        10 ** 1000,
        (0, 1),
        (1, False),
        (1, math.inf),
        ("1", 2),
    ],
)
def test_request_rejects_invalid_timeout_before_pool_request(value):
    client = client_with_capturing_pool()

    with pytest.raises(ApiValueError, match="Request timeout"):
        client.request(
            "GET",
            "https://api.twilio.com",
            _request_timeout=value,
        )

    assert client.pool_manager.calls == []
