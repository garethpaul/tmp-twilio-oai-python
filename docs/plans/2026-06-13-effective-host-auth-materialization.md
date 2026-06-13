# Effective Host Auth Materialization

## Status: Planned

## Context

Basic authentication is filtered at request dispatch using the effective
operation host. `Configuration.auth_settings()` still omits the credential
setting based on the configured default host before dispatch runs. When a
disallowed default host is overridden by a trusted HTTPS operation host, the
dispatch layer has no credential setting left to evaluate or apply.

## Priority

Materialize valid runtime credentials independently of the default host, then
make the existing effective-host dispatch guard the single authorization
decision point.

## Requirements

- R1. Keep blank runtime credentials unable to create a Basic auth setting.
- R2. Make nonblank Basic credentials available for dispatch host evaluation.
- R3. Send auth for a trusted HTTPS override even when the configured default
  host is non-local plain HTTP.
- R4. Continue suppressing auth for non-local HTTP and non-HTTP effective
  hosts, while preserving HTTPS and local HTTP behavior.
- R5. Add no-network regression and static coverage, hostile mutations,
  documentation, and full `make check` verification.

## Implementation Units

### Dispatch-owned host decision

**Files:** `openapi_client/configuration.py`, `test/test_auth_configuration.py`

Return the Basic auth setting whenever trimmed runtime credentials are present;
retain all host filtering in `ApiClient.update_params_for_auth()` and cover a
disallowed default host with an allowed operation override.

### Contracts and maintenance record

**Files:** `scripts/check_docs_plans.py`, `README.md`, `SECURITY.md`,
`VISION.md`, `CHANGES.md`,
`docs/plans/2026-06-13-effective-host-auth-materialization.md`

Reject reintroduced default-host prefiltering, removed dispatch filtering,
missing override coverage, documentation drift, and stale plan status.

## Verification Plan

- focused `test/test_auth_configuration.py` execution
- full pinned Python 3.12 `make check`
- external-working-directory exact-source validation
- focused auth-materialization mutations
- wheel/source content, artifact, secret-pattern, and `git diff --check` audits

## Scope Boundaries

- Do not change the scheme/localhost trust policy, credential trimming,
  generated endpoint signatures, query auth, content routing, or live API use.
- Do not use Twilio credentials or make network requests.
