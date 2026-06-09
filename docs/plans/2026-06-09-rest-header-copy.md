# REST Header Copy Guard

## Status: Completed

## Context

`RESTClientObject.request()` prepares generated request headers before handing
the request to urllib3. The method can add a default `Content-Type` header and,
for multipart uploads, remove that header so urllib3 can generate the boundary.
Those internal mutations should not change a dictionary supplied by the caller.

## Objectives

- Preserve generated REST request behavior.
- Keep caller-owned header dictionaries unchanged.
- Cover default content-type and multipart header preparation without live
  network calls.

## Work Completed

- Copied incoming request headers before applying generated request defaults.
- Added no-network regression tests for default content-type handling and
  multipart header stripping.
- Extended `make lint` syntax coverage to include `openapi_client/rest.py`.
- Extended the docs-plan checker with a source guard for the header copy.
- Updated README, VISION, and CHANGES.

## Verification

- Negative check before implementation:
  `python3 -m pytest -q test/test_rest_request_headers.py` failed because the
  caller header dictionary gained `Content-Type` and then lost multipart
  `Content-Type`.
- `python3 -m pytest -q test/test_rest_request_headers.py`
- `python3 scripts/check_docs_plans.py`
- `python3 -m py_compile setup.py openapi_client/configuration.py openapi_client/api_client.py openapi_client/rest.py`
- `make check`
- `make verify`
- `git diff --check`
