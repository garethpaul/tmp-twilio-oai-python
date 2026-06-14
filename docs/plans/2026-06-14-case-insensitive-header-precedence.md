# Case-Insensitive Header Precedence

## Status: Planned

## Context

Operation headers override client defaults only when dictionary keys have the
same casing. HTTP header names are case-insensitive, so `authorization` can
currently coexist with a default `Authorization`, leaving ambiguous request
authentication material.

## Priority

High request integrity. The operation-specific header must be the sole winner
for an HTTP-equivalent name before transport dispatch.

## Requirements

- Merge client defaults and operation headers case-insensitively.
- Preserve operation-header spelling and value for conflicts.
- Preserve unrelated defaults and operation headers.
- Do not mutate caller-owned or client-default mappings.
- Reject non-string header names through the existing request boundary.
- Add direct dispatch regressions, fail-closed contracts, maintained docs, and
  completed verification evidence.

## Scope Boundaries

- Do not normalize all emitted header casing, change authentication schemes,
  REST content routing, generated API signatures, dependencies, or live Twilio
  behavior.

## Verification

- focused API client header regressions and full offline suite
- repository and external-directory pinned `make check`
- hostile case-folding, explicit-winner, spelling, default-retention,
  input-mutation, documentation, and plan-status mutations
- generated-artifact, credential-pattern, exact-diff, and staged-path audits

## Risks

- Live Twilio API behavior remains intentionally untested without credentials.
