# Changes

## 2026-06-09

- Copied REST request headers before applying generated defaults so caller-owned
  dictionaries are not mutated.
- Added no-network regression coverage for REST header immutability.
- Prevented Basic auth headers from being attached to non-local plain HTTP hosts
  while preserving HTTPS and local-development hosts.
- Initialized missing query parameter lists before applying query-based auth
  settings.
- Added no-network regression coverage for query auth on requests that start
  without query parameters.
- Preserved `ApiException` instances when response bodies are missing or
  already decoded.
- Added no-network regression coverage for `None`, string, and bytes exception
  bodies.

## 2026-06-08

- Trimmed runtime Basic auth credentials and rejected whitespace-only username
  or password values with no-network regression coverage.
- Prevented blank Basic auth username/password values from emitting
  Authorization headers, with no-network regression coverage.
- Added `make check` as the shared repository verification alias.
- Added no-network auth smoke tests confirming generated clients do not send an
  Authorization header by default and only build Basic auth from runtime
  credentials.
- Added a Makefile verification gate for Python syntax checks, full pytest, and
  package metadata checks.
- Added regression coverage for generated client host defaults.
- Changed the generated default host from `/` to `https://api.twilio.com`.
- Added package repository metadata and verified generated Python artifacts stay
  ignored by the existing ignore rules.
- Added canonical `docs/plans` coverage and a docs-plan checker under
  `make check`.
