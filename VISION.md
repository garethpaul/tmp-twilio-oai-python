## Tmp Twilio OAI Python Vision

Tmp Twilio OAI Python is a generated Python client for the public Twilio REST
API produced by OpenAPI Generator.

The repository is useful as a generated-client artifact: it includes generated
models, endpoint docs, tests, packaging metadata, and OpenAPI generator
metadata for inspection and experimentation.

The goal is to preserve generator provenance and make any manual changes
obvious, testable, and easy to regenerate.

The current focus is:

Priority:

- Preserve generated source, docs, and test structure
- Keep OpenAPI Generator metadata available
- Avoid hand-editing generated files without a regeneration note
- Keep credentials as runtime configuration only
- Avoid emitting auth headers from missing, blank, or whitespace runtime credentials
- Avoid sending Basic auth credentials to non-local plain HTTP hosts
- Keep generated auth parameter mutation safe when query strings start empty
- Avoid mutating caller-owned REST request headers
- Keep write-method query strings valid when operation URLs already include
  query parameters
- Preserve repeated query parameter values during write request URL preparation
- Preserve API exceptions when response bodies are missing or already decoded
- Keep completed maintenance plans under `docs/plans`

Next priorities:

- Document the exact OpenAPI input spec and generator command
- Add a regeneration script or Makefile target
- Clarify whether the repository is temporary, experimental, or maintained
- Expand smoke tests that do not call live Twilio APIs

Contribution rules:

- One PR = one focused generator, spec, packaging, test, or documentation change.
- Do not commit Twilio credentials, account SIDs, tokens, or live API outputs.
- Separate generated refreshes from manual patches.
- Record generator version changes.

## Security And Responsible Use

Canonical security policy and reporting:

- [`SECURITY.md`](SECURITY.md)

Generated API clients can perform real account operations. Examples should use
placeholders, tests should avoid live network calls by default, and credential
configuration should remain explicit.

## What We Will Not Merge (For Now)

- Checked-in credentials or account data
- Manual generated-code edits without provenance
- Live-account tests as the only verification path
- Basic auth over non-local plain HTTP hosts
- Error handling that masks generated client API exceptions
- Claims of support without a regeneration process

This list is a roadmap guardrail, not a permanent rule.
Strong user demand and strong technical rationale can change it.
