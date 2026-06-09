# Write Query Append Guard

## Status: Completed

## Context

`RESTClientObject.request` appended write-method query parameters by adding
`?` directly to the URL. That worked for URLs with no query string, but it
created malformed URLs when the base operation URL already included a query
component. Generated clients should preserve any existing query string and add
new parameters with `&`.

## Objectives

- Preserve existing query strings on POST, PUT, PATCH, OPTIONS, and DELETE
  requests.
- Append generated query parameters with `&` when the URL already contains a
  query component.
- Keep the behavior no-network testable through the request capture helper.
- Extend static plan checks so the guard remains part of `make check`.

## Work Completed

- Added `_append_query_params` to centralize write-method URL query handling.
- Updated write-method request preparation to use the helper instead of
  concatenating `?` unconditionally.
- Added a no-network regression test for a POST request whose URL already has a
  query string.
- Updated README, VISION, CHANGES, and docs-plan validation.

## Verification

- `python3 -m pytest -q test/test_rest_request_headers.py`
- `python3 scripts/check_docs_plans.py`
- `make check`
- `git diff --check`

## Follow-Up Candidates

- Add generated endpoint smoke coverage for operations that combine server URLs
  and auth/query parameters.
- Document the exact OpenAPI generator command used to produce the client.
