# REST Response Logging Privacy

## Status: Completed

## Context

The generated REST client wrote every preloaded response body verbatim to its
debug logger. Twilio response and error payloads can contain account metadata,
message content, phone numbers, or credential-adjacent values, so enabling
debug diagnostics could persist sensitive API content in local or hosted logs.

## Priority

Response logging is a privacy boundary for a credentialed API client. Callers
still need enough metadata to correlate transport activity, but raw payloads
should remain available only through the response and exception APIs rather
than being copied implicitly into logs.

## Requirements

- R1. Preloaded success and error responses must not write body content to the
  `openapi_client.rest` logger.
- R2. Debug diagnostics must retain the response status and byte count.
- R3. Public response objects and API exception bodies must remain unchanged.
- R4. No-network tests and the repository contract must protect both success
  and error behavior.

## Work Completed

- Replaced the raw response-body debug message with status and byte-count
  metadata.
- Added no-network regressions for successful and unauthorized responses whose
  payloads contain a sentinel secret.
- Required the metadata-only log statement, privacy assertions, tests, and
  this completed plan in the documentation checker.
- Updated security, maintenance, vision, and change documentation.

## Verification

- `python3 -m pytest -q test/test_rest_response_logging.py`
- `python3 scripts/check_docs_plans.py`
- `make check`
- Negative mutations restoring body logging or removing either privacy test
- `git diff --check`

The tests use an in-memory pool manager and do not contact Twilio or use
credentials.
