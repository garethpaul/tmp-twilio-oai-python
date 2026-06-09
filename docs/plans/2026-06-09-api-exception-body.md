# API Exception Body Preservation

## Status: Completed

## Context

The generated API client caught `ApiException` and blindly decoded
`exception.body` as bytes before re-raising. That masks the original API error
when the body is `None` or already a decoded string, because decoding raises a
new `AttributeError`.

## Objectives

- Preserve the original `ApiException` object on request failures.
- Decode byte response bodies without touching `None` or string bodies.
- Cover the behavior with no-network regression tests.

## Work Completed

- Updated `ApiClient.__call_api` to decode only byte exception bodies.
- Re-raised the original exception with the existing traceback.
- Added tests for `None`, string, and bytes exception bodies.
- Updated README, VISION, and CHANGES.

## Verification

- `python -m pytest -q test/test_api_exception_body.py`
- `python -m py_compile openapi_client/api_client.py`
- `make check`
- `make verify`
- `git diff --check`

## Follow-Up Candidates

- Add no-network tests for response deserialization failures.
- Record the generator command so manual patches can be replayed or removed
  during regeneration.
