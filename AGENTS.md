# AGENTS.md

## Repository purpose

`garethpaul/tmp-twilio-oai-python` is a Python project. twilio-oai generated python lib

## Project structure

- `Makefile` - repository verification targets
- `scripts` - baseline checks and helper scripts
- `docs` - plans, notes, and generated README assets
- `test` - tests and fixtures
- `requirements.txt` - Python runtime dependencies
- `openapi_client` - repository source or sample assets
- `plans` - repository source or sample assets

## Development commands

- Supported runtime: Python 3.10 or newer
- Install dependencies: `python3 -m pip install -r requirements.txt -r requirements-dev.txt`; `python3 -m pip install -e .`
- Full baseline: `make check`
- Combined verification: `make verify`
- Lint/static checks: `make lint`
- Tests: `make test`
- Build: `make build`
- If a command above skips because a platform toolchain is missing, verify on a machine with that SDK before claiming platform behavior is tested.

## Coding conventions

- Language mix noted in the README: Python (120), shell (1).
- Prefer dependency-free tests or stdlib checks when legacy packages are unavailable.

## Testing guidance

- Test-related files detected: `plans/2026-06-08-runtime-auth-smoke-tests.md`, `test/`, `test-requirements.txt`, `test/test_api_exception_body.py`, `test/test_api_v2010_account.py`, `test/test_api_v2010_account_address.py`, `test/test_api_v2010_account_address_dependent_phone_number.py`, `test/test_api_v2010_account_application.py`, `test/test_api_v2010_account_authorized_connect_app.py`, `test/test_api_v2010_account_available_phone_number_country.py`
- Start with the narrowest relevant test or Make target, then run `make check` before handing off if the change is not documentation-only.
- Keep README verification notes in sync when commands, fixtures, or supported toolchains change.

## PR / change guidance

- Keep diffs focused on the requested repository and avoid unrelated modernization or formatting churn.
- Preserve public APIs, sample behavior, file formats, and documented environment variables unless the task explicitly changes them.
- Update tests, README notes, or docs/plans when behavior, security posture, or validation commands change.
- Call out skipped platform validation, legacy toolchain assumptions, and any risky files touched in the final summary.

## Safety and gotchas

- Detected references to Twilio. Keep API keys, OAuth credentials, tokens, and account-specific values in local configuration only.
- Text responses use declared charsets with replacement decoding and fall back to UTF-8 replacement for unknown charsets.
- Preloaded responses enforce a configurable 5 MiB decoded body limit by default; use explicit streaming for intentional larger transfers.
- See `SECURITY.md` for vulnerability reporting and safe research guidance.
- See `VISION.md` for project direction and contribution guardrails.
- See `docs/plans/2026-06-08-tmp-twilio-oai-python-baseline.md` for the canonical generated-client verification baseline.
- See `docs/plans/2026-06-08-nonempty-basic-auth.md` for the Basic auth blank-credential guard.
- See `docs/plans/2026-06-08-trim-basic-auth.md` for the whitespace credential guard.

## Agent workflow

1. Inspect the README, Makefile, manifests, and the files directly related to the request.
2. Make the smallest source or docs change that satisfies the task; avoid generated, vendored, or local-environment files unless required.
3. Run the narrowest useful validation first, then `make check` or the documented package/platform gate when available.
4. If a required SDK, service credential, or external runtime is unavailable, record the skipped command and why.
5. Summarize changed files, commands run, and remaining risks or follow-up validation.
