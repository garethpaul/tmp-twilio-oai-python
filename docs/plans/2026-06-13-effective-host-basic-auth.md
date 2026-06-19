# Effective Host Basic Auth Guard

## Status: Completed

## Context

`Configuration.auth_settings()` decides whether Basic auth is allowed by
examining `configuration.host`. `ApiClient.call_api()` can separately receive
an operation-level `_host` override and sends the request there after auth has
already been attached. A non-local plain HTTP override can therefore bypass
the existing host-scheme guard and receive Twilio credentials.

## Requirements

- Evaluate Basic auth eligibility against the effective request host, including
  operation-level `_host` overrides.
- Preserve Basic auth only when the effective request origin matches the
  configured HTTPS Twilio origin, including normalized default ports.
- Preserve explicitly allowed local HTTP development hosts only when they are
  also the configured origin.
- Suppress Basic auth for non-local plain HTTP overrides before transport.
- Preserve existing direct `update_params_for_auth()` callers by defaulting to
  the configured host when no effective host is supplied.
- Add no-network tests that inspect dispatched headers for same-origin HTTPS,
  cross-origin HTTPS, local HTTP, and non-local HTTP override cases.
- Extend the dependency-free source contract and security documentation.

## Non-Goals

- Do not send requests to Twilio or any external host.
- Do not change credential formats, endpoint generation, TLS verification, or
  the local-host allowlist. Redirects must independently strip sensitive
  headers.
- Do not regenerate the full OpenAPI client.

## Implementation

1. Let the configuration auth helpers evaluate an explicit host while retaining
   the configured-host default.
2. Resolve the effective request host before applying auth in `call_api()` and
   pass it through `update_params_for_auth()`.
3. Add focused no-network dispatch tests and static mutation-resistant guards.
4. Update README, security posture, vision, and change history.

## Verification

- Focused auth and query-auth tests passed 11 tests without network access.
- The full offline suite passed 375 tests under Python 3.12.8.
- The pinned Python 3.12 `make check` gate passed twice in a disposable
  exact-source snapshot, including 375 tests, source and wheel builds, isolated
  wheel import, `pip check`, and `pip-audit` with no known vulnerabilities.
- The second full gate was invoked from `/tmp`, confirming caller-directory
  independence without deleting or overwriting repository build outputs.
- Ten hostile mutations for effective-host selection, scheme restrictions,
  auth propagation, URL selection, insecure override coverage, documentation,
  and plan completion were rejected with focused diagnostics.
- Exact diff, generated-artifact, secret-pattern, and worktree audits passed;
  ignored bytecode caches were preserved and excluded from the commit.
