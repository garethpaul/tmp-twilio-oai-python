# Changes

## 2026-06-08

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
