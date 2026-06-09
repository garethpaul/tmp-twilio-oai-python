# Trim Basic Auth

## Status: Completed

## Context

The generated configuration already skipped Basic auth when username or
password was missing or an empty string. Whitespace-only values were still
truthy, so accidentally blank environment values could produce an
`Authorization` header. Leading or trailing whitespace around real credentials
also produced malformed headers.

## Objectives

- Preserve runtime-only Twilio credential configuration.
- Reject whitespace-only usernames or passwords before building Basic auth.
- Trim surrounding whitespace from runtime credentials before encoding them.
- Cover the behavior with no-network tests.

## Work Completed

- Normalized `Configuration.get_basic_auth_token()` to strip username and
  password before validation and encoding.
- Extended blank-credential tests to include whitespace-only values.
- Added a regression test proving surrounding whitespace is trimmed before
  encoding the Basic auth header.
- Updated README, VISION, and CHANGES.

## Verification

- `python3 -m pytest -q test/test_auth_configuration.py`
- `python3 -m py_compile openapi_client/configuration.py`
- `make check`
- `make verify`
- `git diff --check`

## Follow-Up Candidates

- Add an HTTPS-host guard before sending Basic auth to non-local endpoints.
- Document the exact OpenAPI input spec and generator command.
