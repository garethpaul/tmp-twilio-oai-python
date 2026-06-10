# REST Transport Errors

## Status: Completed

## Context

The generated REST adapter translated TLS errors into `ApiException`, but
timeouts, connection failures, proxy errors, and exhausted retries escaped as
raw urllib3 exceptions. Callers therefore needed two unrelated exception
contracts for failures from the same client request path.

## Work Completed

- Wrapped the broader urllib3 `HTTPError` transport family in
  `ApiException(status=0)`.
- Preserved each original urllib3 exception through Python exception chaining.
- Added a no-network read-timeout regression test for status, reason, and cause.
- Extended the static package contract to protect transport normalization and
  cause preservation.

## Verification

- `make check`
- Negative transport-wrapper and exception-chain source mutations
- `git diff --check`
