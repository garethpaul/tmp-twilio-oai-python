# Changes

## 2026-06-10

- Normalized urllib3 transport failures into `ApiException(status=0)` while
  preserving the original exception cause, with a no-network timeout test.
- Added an isolated install/import smoke test for the built wheel and made the
  Makefile verification paths independent of the caller's working directory.
- Scoped vulnerability auditing to the declared runtime dependency graph and
  added dependency consistency checks with ambient `PYTHONPATH` removed.
- Fixed CI to Ubuntu 24.04, added concurrency cancellation, and annotated
  immutable action pins with their verified release versions.
- Raised the supported Python floor to 3.10 and added a maintained-runtime CI
  matrix through Python 3.14.
- Added pinned runtime and verification requirements, PEP 517 source/wheel
  builds, and dependency auditing to `make check`.
- Pinned pip 26.1.2 in the verification environment to remediate
  `PYSEC-2026-196` in hosted runner images.
- Added least-privilege GitHub Actions verification with immutable action pins.
- Removed stale Travis and GitLab matrices that only targeted unsupported
  Python 3.6 through 3.9 releases.

## 2026-06-09

- Rejected unsupported REST methods with an explicit `ApiValueError` before
  calling urllib3, including no-network regression coverage.
- Preserved repeated query parameter values when write requests append generated
  query params into URLs.
- Fixed write-method query parameter appending so URLs with existing query
  strings use `&` instead of a second `?`.
- Added no-network regression coverage for write requests with existing query
  strings.
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
