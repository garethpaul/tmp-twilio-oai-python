# Operation Header Precedence

## Status: Completed

## Context

`ApiClient` currently updates operation headers with client defaults. A global
default therefore overwrites an endpoint-specific header, including
`Content-Type`, and can change request-body routing at dispatch time.

## Priority

Generated operation metadata is the request-specific contract. Client defaults
should fill missing values without overriding or mutating explicit headers.

## Requirements

- Seed request headers from client defaults.
- Let operation-specific headers win on exact-name conflicts.
- Preserve unrelated default headers.
- Do not mutate the operation header dictionary supplied by the caller.
- Preserve cookie, authentication, serialization, content-type ambiguity,
  effective-host, timeout, and transport behavior.
- Add offline dispatch regressions, fail-closed static contracts, and
  maintained documentation.

## Verification

- The focused header-precedence regression passed, and the complete offline
  suite passed with 377 tests.
- The repository and external-directory pinned `make check` passed.
- Seven hostile header-precedence mutations were rejected: merge-order,
  default-retention, explicit-winner, input-mutation, documentation,
  suite-contract, and plan-status.
- Source and wheel builds, isolated wheel import, `pip check`, and `pip-audit`
  passed. Final artifact, credential, and exact-diff audits also passed.

## Scope Boundary

This change does not make header names case-insensitive in `ApiClient`, alter
the REST layer's duplicate `Content-Type` rejection, or call the live Twilio
API.
