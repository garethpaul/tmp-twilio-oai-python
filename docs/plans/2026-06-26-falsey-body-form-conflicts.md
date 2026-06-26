# Falsey Body and Form Conflicts

Status: Completed

## Context

`RESTClientObject.request()` rejected simultaneous `post_params` and `body`
only when the body was truthy. Explicit JSON bodies such as `False`, `0`, an
empty string, or an empty container therefore bypassed the conflict guard.
Routing then silently ignored form fields, while an empty bytes body under JSON
content type exposed an unrelated raw serialization error.

## Design

- Treat `body=None` as the only absent-body state.
- Reject non-empty form fields with every other explicit body value.
- Preserve the existing exception type and message.
- Preserve ordinary form requests, JSON requests, header copying, content-type
  routing, transport errors, and generated public signatures.

## Test First

A parameterized no-network regression supplied form fields with `False`, `0`,
empty text, empty bytes, an empty mapping, and an empty list. All six cases
failed before implementation because the expected `ApiValueError` was not
raised; the empty-bytes case instead leaked a JSON `TypeError`.

## Verification

- Run the focused request-header pytest cases.
- Run pinned `make check` from the checkout and an external directory.
- Run the complete supported Python package gate and artifact smoke test.
- Reject a mutation restoring body truthiness semantics.
- Run Python compilation and `git diff --check`.
- Use hosted Python 3.10/3.12/3.14 and CodeQL as exact-head authority.

## Scope Boundaries

- No endpoint model, authentication, URL, timeout, response, dependency,
  packaging, workflow, or live Twilio behavior change.
- This is a maintained hardening patch in generated transport code and must be
  preserved by any future generator template or regeneration workflow.

## Verification Completed

- The six-case focused regression failed on the prior truthiness guard and then
  passed after explicit `body is not None` handling.
- Twelve focused request-routing tests passed after implementation.
- The truthiness-restoration mutation was rejected by all six cases.
- Pinned `make check` passed with 427 tests, source/wheel builds, isolated wheel
  import, dependency consistency, and no known audit findings under `C`,
  `C.UTF-8`, and from an external working directory.
- Python compilation and `git diff --check` passed.
- Hosted exact-head and review evidence will be recorded in the PR.
