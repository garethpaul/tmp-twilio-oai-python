# Checkout Credential Isolation

Status: Completed

## Problem

The hosted verification workflow used read-only repository permissions but
left the checkout action's temporary GitHub credential persisted in the local
Git configuration for later steps. The verification commands do not need to
push or otherwise authenticate back to the repository.

## Requirements

- Disable persisted checkout credentials explicitly.
- Keep the immutable checkout action pin and read-only workflow permissions.
- Make the shared repository checker reject removal of the credential guard.
- Preserve the generated client, package metadata, and no-network test scope.

## Evidence

- The workflow configures `persist-credentials: false` on its only checkout.
- The documentation-plan checker inspects every active checkout step and
  requires the credential-isolation setting directly in that step's `with`
  mapping; comments, unrelated steps, missing guards, and duplicate overrides
  are rejected.
- The pinned Python 3.12 repository and external-directory `make check` gates
  passed with 413 tests, package smoke installation, dependency consistency,
  and vulnerability auditing.

## Residual Risk

GitHub-hosted execution still depends on the configured Actions trust boundary
and immutable third-party action pins. No live Twilio credential or request was
used during verification.
