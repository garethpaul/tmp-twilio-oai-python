# Runtime Auth Smoke Tests

## Problem

Generated Twilio clients can perform live account operations when credentials
are configured. The repository had a default-host regression test, but no
no-network coverage proving Authorization headers are absent by default and only
created from explicit runtime credentials.

## TDD Evidence

1. Added `test/test_auth_configuration.py` to exercise `ApiClient` auth
   parameter wiring without making network calls.
2. Verified a default `Configuration()` does not add an Authorization header for
   the Twilio basic-auth setting.
3. Verified `Configuration(username=..., password=...)` produces the expected
   Basic auth header and does not add query credentials.

## Verification

- `make lint`
- `make test`
- `make verify`
- `git diff --check`
