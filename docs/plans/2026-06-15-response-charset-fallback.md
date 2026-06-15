---
title: Response Charset Fallback
type: reliability
status: planned
date: 2026-06-15
---

# Response Charset Fallback

## Problem Frame

`ApiClient.call_api` strictly decodes text response bytes with the charset token
from `Content-Type`. An unknown charset raises `LookupError`, while malformed
bytes raise `UnicodeDecodeError`, preventing normal response deserialization and
discarding otherwise usable payload context.

## Priorities

1. P0: Make unknown response charsets fall back to UTF-8 replacement decoding.
2. P1: Replace malformed byte sequences for known charsets instead of raising.
3. P2: Preserve binary, file, and non-preloaded response behavior unchanged.

## Scope Boundaries

- Add a small text-response decoding helper in `openapi_client/api_client.py`.
- Add captured-response regressions for valid, unknown, and malformed charset
  inputs.
- Extend the maintained package gate and project guidance.
- Do not change requests, authentication, status handling, streaming,
  deserialization types, generated endpoint models, dependencies, or packaging.
- Do not claim live Twilio API execution or credential validation.

## Implementation Units

### U1: Defensive Text Decoding

Decode with the declared charset using replacement error handling. If the
charset is unknown, retry with UTF-8 replacement. Apply the helper only where
the existing client decodes preloaded non-file, non-bytes responses.

### U2: Mutation-Sensitive Verification

Add focused tests that prove valid declared charsets remain honored, malformed
bytes are replaced, unknown charsets fall back, and binary/streaming paths do
not enter text decoding. Require the helper, integration, tests, guidance, and
completed evidence from the package gate.

### U3: Maintained Guidance

Update `AGENTS.md`, `README.md`, `SECURITY.md`, `VISION.md`, `CHANGES.md`, and
this plan with the response-decoding boundary and its offline verification
limits.

## Verification Plan

- Prove unknown-charset and malformed-byte regressions fail before the helper.
- Run focused tests and the full pinned package gate with explicit timeouts.
- Run the full gate from the repository root and an external directory.
- Reject isolated helper, fallback, replacement, integration, test, guidance,
  and completed-plan mutations.
- Audit exact intended paths, generated artifacts, dependency/vendor drift,
  whitespace, conflict markers, and credential-shaped additions.

