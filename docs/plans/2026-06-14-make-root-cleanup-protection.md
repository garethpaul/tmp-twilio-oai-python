# Make Root Cleanup Protection

## Status: Planned

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
