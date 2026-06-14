# Auth Header Case Precedence

## Status: Planned

## Context

Client defaults and operation headers are collapsed case-insensitively before
dispatch, but configured authentication is materialized afterward. A caller's
lowercase `authorization` can therefore coexist with generated
`Authorization`, leaving ambiguous credential material at transport time.

## Priority

High request integrity. Generated authentication already has final precedence
for exact-cased names and must retain that precedence for all HTTP-equivalent
header spellings.

## Requirements

- Remove existing HTTP-equivalent header names before inserting generated
  header authentication.
- Preserve the generated auth header's configured spelling and value.
- Preserve effective-host Basic auth gating and the no-auth path.
- Do not mutate caller-owned operation headers or client defaults.
- Preserve existing default, operation, cookie, content routing, query auth,
  and live-request behavior.
- Add focused dispatch regressions, fail-closed static contracts, maintained
  documentation, mutation coverage, and completed verification evidence.

## Scope Boundaries

- Do not change credential encoding, allowed hosts, auth scheme definitions,
  public generated API signatures, dependencies, or live Twilio behavior.
- Do not send live requests or use real Twilio credentials.

## Implementation Units

1. Add a narrow case-insensitive header assignment helper in `ApiClient`.
2. Use it when materializing header and cookie auth settings.
3. Extend auth dispatch tests, static contracts, and maintained docs.

## Verification

- focused auth/header precedence regressions and full offline suite
- repository and external-directory pinned `make check`
- hostile case-folding, generated-winner, spelling, input-immutability,
  effective-host, documentation, and plan-status mutations
- generated-artifact, credential-pattern, exact-diff, and staged-path audits

## Risks

- Live Twilio API behavior remains intentionally untested without credentials.
