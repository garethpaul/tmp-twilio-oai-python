# Unsupported REST Method Guard

## Status: Completed

## Context

`RESTClientObject.request()` validated supported HTTP methods with `assert`.
Python removes assertions when running with optimization enabled, so an
unsupported method could reach the urllib3 pool manager instead of failing at
the generated client boundary.

## Objectives

- Reject unsupported HTTP methods regardless of Python optimization mode.
- Keep the error explicit and local to REST request preparation.
- Avoid live network calls in the regression coverage.
- Extend the docs-plan checker so the guard remains visible in `make check`.

## Work Completed

- Replaced the method assertion with an `allowed_methods` check that raises
  `ApiValueError`.
- Added a no-network regression test that verifies unsupported methods never
  call the pool manager.
- Extended `scripts/check_docs_plans.py` to require the plan and explicit method
  validation.
- Updated README, VISION, and CHANGES.

## Verification

- Negative: source review showed `assert method in ...` would be disabled by
  `python -O`.
- `python3 -m pytest -q test/test_rest_request_headers.py`
- `python3 -m py_compile setup.py openapi_client/configuration.py openapi_client/api_client.py openapi_client/rest.py`
- `python3 scripts/check_docs_plans.py`
- `make check`
- `make verify`
- `git diff --check`

## Follow-Up Candidates

- Validate malformed `_request_timeout` values with explicit errors instead of
  silently falling back to no timeout.
- Audit generated request helpers for other validation paths that rely on
  Python assertions.
