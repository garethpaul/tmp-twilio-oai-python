# Non-Empty Basic Auth

## Status: Completed

## Context

The generated Twilio configuration already avoided Basic auth headers when
credentials were omitted, but empty strings still counted as configured
credentials. That allowed `Authorization: Basic Og==` or partially blank Basic
auth headers to be generated from accidental runtime configuration.

## Objectives

- Preserve generated client behavior for valid runtime credentials.
- Avoid emitting Basic auth headers from missing or blank username/password
  values.
- Keep the regression covered by no-network tests.
- Document the manual generated-client patch.

## Work Completed

- Updated `Configuration.get_basic_auth_token()` to return `None` unless both
  Basic auth parts are non-empty.
- Updated `Configuration.auth_settings()` to reuse the token helper result.
- Added no-network regression coverage for blank username/password values.
- Updated README, VISION, and CHANGES.

## Verification

- `python3 -m py_compile setup.py openapi_client/configuration.py openapi_client/api_client.py`
- `python3 scripts/check_docs_plans.py`
- `python3 -m pytest -q`
- `python3 setup.py check`
- `make check`
- `make verify`
- `git diff --check`

## Follow-Up Candidates

- Add a regeneration patch note if the OpenAPI generator output is refreshed.
- Consider a static checker for generated-client security patches that must
  survive future regeneration.
