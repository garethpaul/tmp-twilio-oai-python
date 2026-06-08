from openapi_client.configuration import Configuration


def test_default_host_uses_twilio_api():
    assert Configuration().host == "https://api.twilio.com"


def test_explicit_host_overrides_default():
    assert Configuration(host="https://example.test").host == "https://example.test"
