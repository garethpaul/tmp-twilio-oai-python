# Built Wheel Artifact Verification

Status: Completed

## Goal

Make the shared package gate prove that the generated client wheel can be
installed and imported, while keeping dependency results independent of
unrelated packages exposed by a developer or runner environment.

## Changes

- Added a package-artifact checker that requires exactly one built wheel.
- Installed the wheel without dependencies into a temporary target and
  imported it under isolated Python.
- Verified the imported module comes from the temporary installation and
  exposes package version `1.0.0`.
- Added `pip check` with ambient `PYTHONPATH` removed.
- Scoped `pip-audit` to the exact runtime requirements file so unrelated local
  development packages do not change the vulnerability result.
- Made Makefile paths resolve from the repository location.
- Fixed CI to Ubuntu 24.04, added concurrency cancellation, and documented the
  release versions behind immutable action commits.
- Extended repository contracts and maintenance documentation for the new
  artifact gate.

## Scope Boundaries

- Preserve generated models, endpoint behavior, and public API signatures.
- Do not publish the package or contact live Twilio services.
- Do not install the built wheel into the caller's active environment.

## Verification

- Fresh virtual environment installation from both requirement files.
- `make check`
- `make -C /path/to/tmp-twilio-oai-python check`
- Direct wheel checker execution after a package build.
- Negative checks for missing wheels, source-tree imports, floating CI runners,
  ambient-environment audits, and omitted dependency consistency checks.
- `git diff --check`
