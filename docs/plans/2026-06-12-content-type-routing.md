# Content-Type Routing

## Status: Completed

## Context

The generated REST transport looks up `Content-Type` with case-sensitive
dictionary access and compares form media types as exact strings. A caller that
supplies a valid lowercase header or a media-type parameter can therefore gain a
second conflicting JSON header or route form data through the wrong encoder.
Multipart cleanup also deletes only the canonical header spelling.

## Priority

Resolve request content type according to HTTP's case-insensitive header rules
before transport dispatch, while preserving caller-header immutability.

## Requirements

- R1. Resolve exactly one Content-Type header case-insensitively and preserve
  its caller-provided spelling in the copied transport headers.
- R2. Add the JSON default only when no case-insensitive Content-Type exists.
- R3. Route JSON, URL-encoded form, and multipart requests by normalized base
  media type so parameters do not change encoder selection.
- R4. Remove the actual caller spelling for multipart so urllib3 can generate
  its boundary, and reject ambiguous duplicate case variants before dispatch.
- R5. Add no-network tests, static contracts, hostile mutations, documentation,
  and full `make check` verification.

## Scope Boundaries

- Do not change generated endpoint methods, authentication, timeout behavior,
  response handling, dependency versions, or hosted workflow.
- Do not contact Twilio or use credentials.
- Keep caller-owned header dictionaries immutable.

## Implementation Units

### Media-type resolution

**Files:** `openapi_client/rest.py`

- Add a small helper that finds a single case-insensitive Content-Type key,
  validates its value, and returns its normalized base media type.
- Use the resolved key for multipart removal and the base type for dispatch.

### Offline contracts and maintenance record

**Files:** `test/test_rest_request_headers.py`, `scripts/check_docs_plans.py`,
`README.md`, `SECURITY.md`, `VISION.md`, `CHANGES.md`,
`docs/plans/2026-06-12-content-type-routing.md`

## Verification Plan

- focused request-header tests
- complete offline pytest suite
- source/wheel build and isolated import
- dependency consistency and runtime audit
- `make check` from the repository and an external directory
- focused Content-Type mutations
- `git diff --check`

## Verification Record

- `python3 -m pytest -q test/test_rest_request_headers.py` passed all nine
  no-network request-header tests.
- `git diff --check` passed after the runtime, test, contract, and documentation
  updates.
- Six focused mutations were rejected across case-insensitive lookup, base
  media-type parsing, multipart header removal, duplicate rejection, and the
  form/duplicate regression tests.
- A disposable source snapshot passed `make check` in the pinned Python 3.12
  environment: 371 offline tests, source and wheel builds, isolated wheel
  import, `pip check`, and `pip-audit` with no known vulnerabilities.
- External-directory `make -f /absolute/path/Makefile check` passed the same
  snapshot gate. No Twilio credentials or live network calls were used.

## Remaining Risks

- Offline tests do not exercise live Twilio endpoints or intermediary header
  rewriting.
- The package remains generated code with manual safety patches that require
  preservation during future regeneration.
