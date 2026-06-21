# Make Cleanup Authority Isolation

Status: Completed

## Goal

Keep generated-package cleanup and repository verification confined to the
checked-out client when Make is invoked from another directory or with hostile
caller variables, startup files, modes, shell overrides, and executable paths.

## Changes

- Resolve and export the repository root from the checked-in Makefile alone.
- Freeze the trusted Python executable override as a literal value and fix the
  recipe shell.
- Reject caller-supplied `MAKEFLAGS`, `MAKEFILES`, `MAKEFILE_LIST`, dry-run,
  touch, question, and ignore-error verification modes.
- Add cleanup sentinels for attacker-controlled build, distribution, and
  egg-info paths across every public target and root/shell authority mode.
- Invoke hosted verification through `/usr/bin/make`.

## Verification

- repository and external-directory pinned `make check` passed
- 35 target/authority cleanup combinations preserved all attacker sentinels
- raw Make-syntax tools, startup boundaries, caller flags, and non-executing or
  error-ignoring modes were rejected
- 419 offline tests, wheel build/smoke, `pip check`, and `pip-audit` passed
