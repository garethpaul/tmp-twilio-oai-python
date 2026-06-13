# Effective Host Basic Auth Guard

## Status: In Progress

## Context

`Configuration.auth_settings()` decides whether Basic auth is allowed by
examining `configuration.host`. `ApiClient.call_api()` can separately receive
an operation-level `_host` override and sends the request there after auth has
already been attached. A non-local plain HTTP override can therefore bypass
the existing host-scheme guard and receive Twilio credentials.

## Requirements

- Evaluate Basic auth eligibility against the effective request host, including
  operation-level `_host` overrides.
- Preserve Basic auth for the configured HTTPS Twilio host, HTTPS overrides,
  and explicitly allowed local HTTP development hosts.
- Suppress Basic auth for non-local plain HTTP overrides before transport.
- Preserve existing direct `update_params_for_auth()` callers by defaulting to
  the configured host when no effective host is supplied.
- Add no-network tests that inspect dispatched headers for HTTPS, local HTTP,
  and non-local HTTP override cases.
- Extend the dependency-free source contract and security documentation.

## Non-Goals

- Do not send requests to Twilio or any external host.
- Do not change credential formats, endpoint generation, redirects, TLS
  verification, or the local-host allowlist.
- Do not regenerate the full OpenAPI client.

## Implementation

1. Let the configuration auth helpers evaluate an explicit host while retaining
   the configured-host default.
2. Resolve the effective request host before applying auth in `call_api()` and
   pass it through `update_params_for_auth()`.
3. Add focused no-network dispatch tests and static mutation-resistant guards.
4. Update README, security posture, vision, and change history.

## Verification

- Run focused auth and query-auth tests.
- Run the pinned Python 3.12 `make check` gate, including 371+ offline tests,
  source/wheel builds, isolated wheel import, `pip check`, and `pip-audit`.
- Run the same gate from outside the repository against a disposable snapshot.
- Reject hostile mutations for effective-host selection, auth propagation,
  insecure override handling, tests, documentation, and plan completion.
- Audit the exact diff, generated artifacts, secret patterns, and worktree.
