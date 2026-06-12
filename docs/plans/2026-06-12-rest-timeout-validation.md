# REST Request Timeout Validation

## Status: Completed

## Context

`RESTClientObject.request()` only constructs an `urllib3.Timeout` when
`_request_timeout` is a number or a two-item tuple. Every other non-empty value
silently leaves `timeout` as `None`, so a misspelled or malformed bounded
request can run with the transport defaults instead of the caller's intended
limit.

## Priority

This client wraps credentialed Twilio API calls. Timeout configuration is a
resource and reliability boundary, and invalid values should fail before any
network work rather than weakening that boundary implicitly.

## Prioritized Engineering Backlog

1. Validate request timeout values explicitly before invoking urllib3.
2. Preserve supported positive total and connect/read timeout forms.
3. Keep transport exception normalization and request serialization unchanged.
4. Document the OpenAPI input and regeneration process in a separate generated
   client maintenance pass.

## Requirements

- R1. `None` must continue to use urllib3's configured/default timeout policy.
- R2. A positive, finite, urllib3-representable non-boolean integer or float
  must produce a total timeout.
- R3. A two-item tuple must produce connect/read timeouts when each component is
  either `None` or a positive non-boolean integer or float.
- R4. Booleans, strings, wrong-length tuples, lists, and non-positive numeric
  values must raise `ApiValueError` before the pool manager is called.
- R5. Tests, docs, the plan checker, and the package gate must preserve the
  timeout validation contract.

## Implementation Units

### U1. Centralize timeout preparation

- **Files:** `openapi_client/rest.py`
- Add a focused helper that validates and constructs `urllib3.Timeout` values.
- Keep `None` distinct from malformed values and reject booleans explicitly.

### U2. Add no-network regressions

- **Files:** `test/test_rest_request_timeout.py`
- Cover accepted total and tuple forms, invalid types and lengths, non-positive
  values, and the guarantee that rejected values never reach the pool manager.

### U3. Preserve repository contracts

- **Files:** `scripts/check_docs_plans.py`, `README.md`, `SECURITY.md`,
  `VISION.md`, `CHANGES.md`
- Record the supported timeout forms and make the static checker require the
  helper, regression tests, and completed plan.

## Scope Boundaries

- Do not add a default timeout policy in this change.
- Do not change retries, proxy settings, TLS configuration, or error wrapping.
- Do not regenerate the generated API surface.

## Verification

- `.venv/bin/python -m pytest -q`
- `.venv/bin/python -m pytest -q test/test_rest_request_timeout.py`
- `.venv/bin/python scripts/check_docs_plans.py`
- `make check` with `PYTHON=.venv/bin/python`
- `.venv/bin/python -m pip check`
- `.venv/bin/python -m pip_audit -r requirements.txt`
- `git diff --check`
- Negative mutations allowing malformed values to reach the pool manager must
  fail the focused tests and static checker.
