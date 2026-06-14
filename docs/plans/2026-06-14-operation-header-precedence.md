# Operation Header Precedence

## Status: Planned

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

- focused header-precedence regressions and complete offline test suite
- repository and external-directory pinned `make check`
- hostile merge-order, default-retention, explicit-winner, input-mutation,
  documentation, suite-contract, and plan-status mutations
- package build/import, dependency, vulnerability, artifact, credential, and
  exact-diff audits

## Scope Boundary

This change does not make header names case-insensitive in `ApiClient`, alter
the REST layer's duplicate `Content-Type` rejection, or call the live Twilio
API.
