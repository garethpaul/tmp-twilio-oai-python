# Make Root Cleanup Protection

## Status: Completed

## Context

The Makefile removes `$(ROOT)/build`, `$(ROOT)/dist`, and root-level egg-info
directories before packaging, but environment and command-line assignments can
replace `ROOT`. A hostile or stale caller value can redirect destructive
cleanup and all subsequent verification outside the checked-out repository.

## Priority

The package cleanup path is a filesystem trust boundary. The repository must
select its own root while preserving the intentional Python executable
override and complete package-quality gate.

## Objectives

- Protect the repository-derived root from caller assignments.
- Preserve root-first ordering and the `PYTHON` override.
- Keep cleanup limited to repository build, distribution, and egg-info paths.
- Preserve all six aliases, 376-test suite, package smoke, compatibility check,
  and runtime vulnerability audit.
- Add mutation-sensitive source, README, and completed-plan contracts.

## Implementation Units

### U1. Protect cleanup and verification paths

**Files:** `Makefile`

Make `ROOT` authoritative without changing the Python override, target graph,
cleanup scope, build command, or audit behavior.

### U2. Preserve the package contract

**Files:** `scripts/check_docs_plans.py`, `README.md`

Require one root assignment total, the exact protected declaration, root-first
tool ordering, aliases, exact cleanup paths, root-anchored build/audit commands,
README indexing, and this plan's completed evidence.

## Verification

- Focused documentation contracts and complete pinned `make check`.
- Repository/external working directories and hostile root assignments.
- Declaration, duplicate, placement, alias, cleanup-path, README, and plan
  mutations.
- Source/wheel content, explicit generated cleanup, exact diff, protected
  package/auth/workflow paths, secrets, and whitespace audits.
- Exact-head Python 3.10, 3.12, and 3.14 hosted verification.

## Scope Boundary

This change does not alter generated client code, authentication, transport,
dependencies, package metadata, workflow policy, or use Twilio credentials or
live API requests.

## Work Completed

- Marked the root-first repository path as an explicit GNU Make override.
- Added exact declaration, ordering, alias, cleanup-path, build, README, and
  plan contracts to the documentation checker.
- Preserved Python override, package behavior, authentication, workflow, and
  audit scope.

## Verification Results

- The isolated pinned Python 3.12.8 `make check` passed 376 offline tests,
  source and wheel builds, isolated wheel import, `pip check`, and `pip-audit`
  with no known vulnerabilities.
- All six public aliases passed from repository and external working
  directories with hostile environment and command-line `ROOT` assignments,
  for 24 cases.
- Hostile build, distribution, and egg-info sentinel files remained intact
  after every package-cleanup target; the explicit Python override remained
  effective.
- Eight protected-declaration, duplicate protected/unprotected assignment,
  placement, alias, cleanup-path, README, and plan mutations were rejected.
- Plan-aware filesystem-safety, security, package-contract, testing,
  maintainability, reliability, and project-standards review found no
  actionable findings.
- Exact diff, protected client/auth/transport/package/workflow path,
  generated-artifact, high-confidence secret, and whitespace audits passed.
- Only explicitly identified validation-created build, distribution, egg-info,
  bytecode, and pytest-cache paths were removed; no Twilio credentials or live
  API calls were used.
