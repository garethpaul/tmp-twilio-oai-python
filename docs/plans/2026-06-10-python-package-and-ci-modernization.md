# Python Package and CI Modernization

Status: Completed

## Goal

Make the generated Twilio client reproducibly installable and continuously
verified on maintained Python releases without broad generated-code churn.

## Changes

- Declare a modern Python support floor and compatible direct dependency bounds.
- Add PEP 517 build metadata and a pinned verification dependency set.
- Upgrade hosted environments to pip 26.1.2 before auditing to remediate
  `PYSEC-2026-196` in the runner-provided pip 26.1.1.
- Build both source and wheel distributions during the shared quality gate.
- Audit the fully resolved declared runtime dependency graph, including
  transitive dependencies, and run all 342 offline regression tests.
- Replace obsolete hosted CI assumptions with a least-privilege GitHub Actions
  matrix using immutable action pins and a manual verification trigger.
- Remove stale Travis and GitLab matrices that only exercised unsupported
  Python 3.6 through 3.9 releases.
- Add repository contracts for dependency versions, packaging, and workflow
  drift.

## Scope Boundaries

- Preserve generated models and public API signatures.
- Do not reformat generated source wholesale.
- Do not call live Twilio services or require credentials.

## Verification

- Fresh virtual environment installation from both requirement files.
- `make check`
- Wheel installation and import smoke test.
- Negative workflow contract mutation.
