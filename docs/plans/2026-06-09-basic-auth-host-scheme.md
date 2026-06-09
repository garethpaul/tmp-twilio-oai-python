# Basic Auth Host Scheme Guard

## Status: Completed

## Context

The generated client now avoids blank or whitespace-only Basic auth headers,
but valid runtime credentials were still eligible for any configured host. That
can leak Twilio credentials if a caller accidentally points the generated
client at a non-local plain HTTP endpoint.

## Objectives

- Preserve Basic auth for the default HTTPS Twilio host.
- Allow local plain HTTP hosts for no-network development and tests.
- Avoid attaching Basic auth to non-local plain HTTP hosts.
- Cover the behavior with no-network regression tests.

## Work Completed

- Added `Configuration.host_allows_basic_auth()` using the configured host
  scheme and local-host allowlist.
- Changed `Configuration.auth_settings()` to emit Basic auth only when the host
  allows it.
- Added no-network tests for non-local HTTP suppression and local HTTP
  allowance.
- Extended the docs-plan checker with source guards for the Basic auth host
  scheme helper.
- Updated README, VISION, and CHANGES.

## Verification

- `python3 -m pytest -q test/test_auth_configuration.py`
- `python3 -m py_compile setup.py openapi_client/configuration.py openapi_client/api_client.py`
- `python3 scripts/check_docs_plans.py`
- `make check`
- `make verify`
- `git diff --check`
