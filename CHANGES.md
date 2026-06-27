# Changes

## 2026-06-26 17:05 PDT - P1 - Reject discarded GET and HEAD bodies

### Summary
Stopped the REST client from silently discarding explicitly supplied bodies or
form fields on `GET` and `HEAD` requests.

### Work completed
- Added fourteen red-first no-network body and form-field regressions.
- Rejected every present body, including falsey JSON values, before dispatch.
- Rejected non-empty form fields while preserving query parameters.
- Bound the source, tests, plan, and generated-client maintenance guidance.

### Threads
- Started: none.
- Continued: generated REST request ownership hardening.
- Stopped: none.

### Files changed
- `openapi_client/rest.py` — owns the body-free read-method boundary.
- `test/test_rest_request_headers.py` — covers GET/HEAD body loss.
- `scripts/check_docs_plans.py` — preserves the regression contracts.
- Documentation and plan files — record behavior and regeneration scope.

### Validation
- Focused pytest — all fourteen cases failed before implementation because the
  pool manager was called without the supplied data.
- `make check PYTHON=.venv/bin/python` — passed 441 tests, source/wheel builds,
  isolated wheel import, `pip check`, and zero known audit findings.
- The complete gate also passed from `/tmp` through the absolute Makefile path.
- Python compilation, documentation contracts, and `git diff --check` — passed.
- Hosted exact-head validation remains next.

### Bugs / findings
- P1 correctness: callers could receive a successful GET or HEAD response even
  though explicitly supplied request data was never transmitted.

### Blockers
- None; tests use an offline capturing transport and no credentials.

### Next action
- Run the complete package gate, review the exact head, and merge the PR.

## 2026-06-26 02:50 PDT - P2 - Reject falsey body/form conflicts

### Summary
Hardened REST request preparation so form fields cannot be combined with an
explicitly supplied body merely because that body is falsey.

### Work completed
- Replaced the body truthiness conflict check with explicit presence semantics.
- Covered `False`, `0`, empty text, empty bytes, empty mappings, and empty lists.
- Preserved requests that supply form fields with the default `body=None`.
- Prevented silent form-field loss and an unwrapped JSON serialization failure
  before urllib3 dispatch.
- Bound the invariant into source and test maintenance contracts.

### Threads
- Started: none.
- Continued: generated REST request integrity — body/form exclusivity complete.
- Stopped: none.

### Files changed
- `openapi_client/rest.py` — rejects form parameters with every present body.
- `test/test_rest_request_headers.py` — adds six no-network falsey-body cases.
- `scripts/check_docs_plans.py` — preserves the source, test, and plan contracts.
- Documentation and plan files — record behavior and offline validation scope.

### Validation
- Red-first focused pytest — all six cases bypassed the old guard; five silently
  discarded form fields and empty bytes raised a raw JSON `TypeError`.
- Focused request-routing tests — twelve passed after implementation.
- Truthiness-restoration mutation — rejected with all six regressions failing.
- `make check PYTHON=.venv/bin/python` — passed with 427 tests, source/wheel
  builds, isolated wheel import, `pip check`, and zero known audit findings.
- The same complete gate passed under `C`, `C.UTF-8`, and from `/tmp` through
  the absolute Makefile path.
- Python compilation and `git diff --check` — passed.
- Hosted Python/CodeQL exact-head checks and review remain the next action.

### Bugs / findings
- P2: `post_params and body` treated falsey bodies as absent, violating the
  documented one-representation request boundary.

### Blockers
- None; validation uses offline fake transports and no Twilio credentials.

### Next action
- Open the focused PR, run exact-head hosted validation and review, then merge.

## 2026-06-25 07:11 PDT

- Decoded byte-backed API exception bodies with their declared response
  charset instead of forcing UTF-8 and corrupting non-ASCII provider details.
- Successful and error text responses use declared charsets with replacement
  decoding and UTF-8 fallback for missing or unknown codecs.
- Added focused runtime plus dependency-free contracts for the error path.

## 2026-06-21

- Disabled persisted GitHub checkout credentials and added a step-aware
  repository contract that rejects comments, unrelated settings, missing
  guards, and duplicate overrides.
- Isolated destructive package cleanup and verification from caller-controlled
  Make roots, shells, startup files, non-executing modes, and tool syntax.
- Added adversarial cleanup sentinels and pinned hosted verification to
  `/usr/bin/make`.

## 2026-06-19

- Bound generated Basic auth to the configured request origin and enforced
  sensitive-header stripping for cross-host redirects.
- Rejected request URL userinfo and header control characters before transport,
  and limited JSON serialization to standard JSON media types.
- Closed non-preloaded error responses without reading unbounded bodies and
  expanded valid response charset parsing.

## 2026-06-16

- Preloaded responses enforce a configurable decoded body limit, defaulting to
  5 MiB, and close oversized transports without changing explicit streaming.

## 2026-06-15

- Text responses use declared charsets with replacement decoding and fall back
  to UTF-8 replacement for unknown charsets.

## 2026-06-14

- Added auth header case precedence so generated credentials replace
  HTTP-equivalent operation header spellings before transport.
- Added case-insensitive header precedence for HTTP-equivalent operation names.
- Fixed operation header precedence so client defaults fill missing values
  without overwriting or mutating endpoint-specific request headers.

## 2026-06-13

- Made the dispatch-time host the single Basic auth authorization decision so
  trusted overrides are not suppressed by an unrelated default host.
- Applied the Basic auth scheme guard to operation-level request host
  overrides so non-local plain HTTP destinations cannot receive credentials.

## 2026-06-12

- Made REST Content-Type resolution case-insensitive and parameter-aware,
  rejected conflicting case variants, and preserved multipart boundary setup.
- Replaced raw REST response-body debug logging with status and byte-count
  metadata, with no-network privacy regressions for success and error payloads.
- Rejected malformed REST request timeout values before invoking urllib3 so an
  intended bounded request cannot silently fall back to transport defaults.
- Added no-network coverage for default, total, connect/read, non-positive,
  non-finite, boolean, and malformed timeout forms.

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
