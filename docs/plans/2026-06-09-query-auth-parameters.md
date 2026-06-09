# Query Auth Parameter Guard

## Status: Completed

## Context

The generated `ApiClient.__call_api` passed `None` into
`update_params_for_auth` when a request had no query parameters. Header-based
auth did not notice, but query-based auth attempted to append to that `None`
value and raised `AttributeError` before the request could be prepared.

## Objectives

- Preserve no-network test coverage for query auth mutation.
- Initialize missing query parameter lists before auth settings are applied.
- Keep the generated client behavior unchanged for requests that already have
  query parameters.

## Work Completed

- Added `test/test_query_auth_parameters.py` with a no-network query-auth
  regression.
- Updated `ApiClient.__call_api` to initialize an empty query list when auth
  settings are present and no query list exists.
- Updated README, VISION, and CHANGES with the new guardrail.

## Verification

- `python3 -m pytest -q test/test_query_auth_parameters.py`
- `make lint`
- `make test`
- `make build`
- `make check`
- `make verify`
- `git diff --check`

## Follow-Up Candidates

- Add no-network tests for query auth combined with existing query parameters.
- Record the generator command so this manual patch can be replayed or removed
  during regeneration.
