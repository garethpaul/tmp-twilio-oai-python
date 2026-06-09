# Repeated Write Query Parameters

## Status: Completed

## Context

Write requests append generated query parameters into the URL before calling
urllib3. `_append_query_params()` preserved existing query strings, but it used
plain `urlencode()`, so list-valued query parameters were serialized as a single
Python list string instead of repeated keys.

## Objectives

- Preserve existing query-string appending behavior for write requests.
- Encode list-valued query parameters as repeated query keys.
- Keep the change no-network and limited to REST request preparation.
- Add regression and static coverage so `doseq=True` remains in place.

## Work Completed

- Changed `_append_query_params()` to call `urlencode(..., doseq=True)`.
- Added a no-network REST client test for repeated write query parameters.
- Extended `scripts/check_docs_plans.py` to preserve the repeated-query guard.
- Updated README, VISION, and CHANGES.

## Verification

- Negative: `python3 -m pytest -q test/test_rest_request_headers.py` failed
  before the helper fix because list-valued query parameters were encoded as a
  single list string.
- `python3 -m pytest -q test/test_rest_request_headers.py`
- `python3 -m py_compile setup.py openapi_client/configuration.py openapi_client/api_client.py openapi_client/rest.py`
- `python3 scripts/check_docs_plans.py`
- `make check`
- `make verify`
- `git diff --check`

## Follow-Up Candidates

- Audit generated endpoints for list-valued query parameters that should use
  the `multi` collection format.
- Add generator template notes if this manual runtime patch is carried forward.
