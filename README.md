# tmp-twilio-oai-python

<!-- README-OVERVIEW-IMAGE -->
![Project overview](docs/readme-overview.svg)

## Overview

`garethpaul/tmp-twilio-oai-python` is a Python project. twilio-oai generated python lib

This README is based on the checked-in source, manifests, scripts, and repository metadata on the `master` branch. The project language mix found during review was: Python (120), shell (1).

## Repository Contents

- `README.md` - project overview and local usage notes
- `CHANGES.md` - maintenance history for generated-client checks
- `Makefile` - local verification entry points
- `requirements.txt` - Python dependency or packaging metadata
- `docs` - source or example code
- `docs/plans` - completed maintenance plans for the current baseline
- `openapi_client` - source or example code
- `plans` - historical implementation notes
- `scripts` - documentation-plan validators
- `SECURITY.md` - security reporting and disclosure guidance
- `setup.py` - Python dependency or packaging metadata
- `test` - source or example code
- `VISION.md` - project direction and maintenance guardrails

Additional scan context:

- Source directories: docs, openapi_client, test
- Dependency and build manifests: requirements.txt, setup.py
- Entry points or build surfaces: none detected
- Test-looking files: test/test_auth_configuration.py, test/test_configuration_defaults.py, generated tests under test/

## Getting Started

### Prerequisites

- Git
- Python 3.10 or newer; CI verifies Python 3.10, 3.12, and 3.14

### Setup

```bash
git clone https://github.com/garethpaul/tmp-twilio-oai-python.git
cd tmp-twilio-oai-python
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
```

The setup commands above are derived from repository files. Legacy mobile, Python, or JavaScript samples may require older SDKs or package versions than a modern workstation uses by default.

## Running or Using the Project

- Import `openapi_client.Configuration` and provide Twilio credentials through
  the generated basic-auth configuration. The default API host is
  `https://api.twilio.com`.

## Testing and Verification

- `make check` runs Python syntax checks, the generated pytest suite, package
  source/wheel builds, an isolated install/import smoke test of the built
  wheel, dependency consistency checks, and a security audit of the declared
  runtime dependency graph, including transitive dependencies. Ambient
  `PYTHONPATH` entries are excluded from dependency verification. The suite has
  380 offline tests.
- The pytest suite includes no-network checks for default host configuration
  and runtime-only, trimmed, non-empty Basic auth headers. It also covers API
  exception body handling so client errors are not masked by response decoding,
  and query auth parameter handling for requests with no preexisting query
  list. Basic auth tests also ensure credentials are not attached to non-local
  plain HTTP hosts, including operation-level host overrides. The dispatch-time
  host remains the single authorization decision even when the configured
  default host differs from an operation override, and REST request tests
  ensure caller-provided header dictionaries are not mutated while defaults
  are prepared. Operation header precedence keeps client defaults as
  fallbacks without replacing endpoint-specific metadata on exact-name
  conflicts. Case-insensitive header precedence also removes differently cased
  defaults when an operation supplies the HTTP-equivalent name. Auth header case precedence
  ensures generated credentials remain the sole final winner even when an
  operation used different casing. Content-Type
  routing is case-insensitive, accepts media-type parameters, and rejects
  ambiguous duplicate spellings before dispatch. REST request tests
  also ensure write methods append query parameters to existing query strings
  with `&`, preserve repeated query parameter values, and reject unsupported
  HTTP methods before invoking urllib3.
- REST transport tests verify timeouts and other urllib3 failures surface
  through the generated client's `ApiException` contract with their cause kept.
- REST request timeout validation accepts positive numeric totals or two-item
  connect/read tuples containing positive numbers or `None`; malformed,
  non-positive, boolean, and non-finite values fail before network work.
- REST debug logging records only response status and byte count; response and
  error bodies remain available to callers without being copied into logs.
- `make check` also requires completed canonical plans under `docs/plans`.
- GitHub Actions runs the same gate on Python 3.10, 3.12, and 3.14 with
  read-only permissions, a fixed Ubuntu 24.04 image, bounded jobs, concurrency
  cancellation, and immutable action pins.
- The verification requirements upgrade pip to 26.1.2 before auditing because
  hosted Python images may include the vulnerable 26.1.1 release.
- Obsolete Travis and GitLab matrices for end-of-life Python releases have been
  removed so the checked-in CI support statement is unambiguous.

When the required SDK or runtime is unavailable, use static checks and source review first, then verify on a machine that has the matching platform toolchain.

## Configuration and Secrets

- Detected references to Twilio. Keep API keys, OAuth credentials, tokens, and account-specific values in local configuration only.

## Security and Privacy Notes

- Review changes touching authentication or token handling; examples from the scan include docs/ApiV2010AccountToken.md, docs/DefaultApi.md, openapi_client/api/default_api.py, openapi_client/api_client.py, and 2 more.
- Review changes touching external API calls or credential-adjacent configuration; examples from the scan include docs/DefaultApi.md, openapi_client/__init__.py, openapi_client/api/default_api.py, openapi_client/api_client.py, and 6 more.
- Review changes touching network requests, sockets, or service endpoints; examples from the scan include .gitlab-ci.yml, .travis.yml, docs/DefaultApi.md, git_push.sh, and 6 more.
- Review changes touching file, media, JSON, XML, CSV, OCR, or data parsing; examples from the scan include .gitlab-ci.yml, docs/DefaultApi.md, openapi_client/api/default_api.py, openapi_client/api_client.py, and 6 more.
- Review changes touching database, model, or persistence code; examples from the scan include docs/ApiV2010Account.md, docs/ApiV2010AccountAddress.md, docs/ApiV2010AccountAddressDependentPhoneNumber.md, docs/ApiV2010AccountApplication.md, and 6 more.
- Review changes touching infrastructure, proxy, cloud, or deployment configuration; examples from the scan include docs/DefaultApi.md, openapi_client/api/default_api.py.

## Maintenance Notes

- See `SECURITY.md` for vulnerability reporting and safe research guidance.
- See `VISION.md` for project direction and contribution guardrails.
- See `docs/plans/2026-06-08-tmp-twilio-oai-python-baseline.md` for the
  canonical generated-client verification baseline.
- See `docs/plans/2026-06-08-nonempty-basic-auth.md` for the Basic auth
  blank-credential guard.
- See `docs/plans/2026-06-08-trim-basic-auth.md` for the whitespace credential
  guard.
- See `docs/plans/2026-06-09-basic-auth-host-scheme.md` for the Basic auth
  host-scheme guard.
- See `docs/plans/2026-06-13-effective-host-basic-auth.md` for the
  operation-level host override credential guard.
- See `docs/plans/2026-06-13-effective-host-auth-materialization.md` for the
  dispatch-time host authorization boundary.
- See `docs/plans/2026-06-09-api-exception-body.md` for the API exception body
  preservation guard.
- See `docs/plans/2026-06-09-query-auth-parameters.md` for the query auth
  parameter initialization guard.
- See `docs/plans/2026-06-09-rest-header-copy.md` for the REST request header
  mutation guard.
- See `docs/plans/2026-06-09-write-query-append.md` for the write request
  query-string append guard.
- See `docs/plans/2026-06-09-repeated-write-query-params.md` for repeated write
  query parameter coverage.
- See `docs/plans/2026-06-09-unsupported-rest-method.md` for unsupported REST
  method validation.
- See `docs/plans/2026-06-10-rest-transport-errors.md` for normalized urllib3
  transport failures and exception chaining.
- See `docs/plans/2026-06-12-rest-timeout-validation.md` for request timeout
  validation before urllib3 dispatch.
- See `docs/plans/2026-06-12-rest-response-logging.md` for metadata-only REST
  response diagnostics and payload privacy coverage.
- See `docs/plans/2026-06-12-content-type-routing.md` for case-insensitive,
  parameter-aware request encoder selection.
- See `docs/plans/2026-06-14-make-root-cleanup-protection.md` for authoritative
  repository-root and package-cleanup selection across all Make aliases.
- See `docs/plans/2026-06-14-operation-header-precedence.md` for request-specific
  header precedence at the API dispatch boundary.
- See `docs/plans/2026-06-14-case-insensitive-header-precedence.md` for
  HTTP-equivalent header conflict handling.
- See `docs/plans/2026-06-14-auth-header-case-precedence.md` for generated
  credential precedence over differently cased operation headers.

## Contributing

Keep changes small and tied to the project that is already present in this repository. For code changes, document the toolchain used, avoid committing generated dependency directories or local configuration, and update this README when setup or verification steps change.
