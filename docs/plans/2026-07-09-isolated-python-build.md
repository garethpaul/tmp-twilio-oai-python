# Isolated Python Package Build

Status: Completed

## Goal

Make `make build` resilient on developer hosts where ambient site-packages
include packages that break non-isolated setuptools egg_info (for example
`pbr` loading without `pkg_resources`).

## Changes

- Drop `python -m build --no-isolation` from the Makefile build target.
- Use the default isolated build backend environment so `pyproject.toml`
  pins for setuptools and wheel are the only build dependencies.
- Keep the Makefile verification contract in `scripts/check_docs_plans.py`
  aligned with the isolated build command.

## Scope Boundaries

- No generated client API changes.
- No dependency version changes beyond build isolation behavior.
- Preserve package-smoke, pip check, and pip-audit gates.

## Verification

- `make check`
- Isolated `python -m build` succeeds on a host where non-isolated build
  previously failed with `ModuleNotFoundError: No module named 'pkg_resources'`.
