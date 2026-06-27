# Reject bodies on REST read methods

Status: Completed

## Context

`RESTClientObject.request()` accepted `body` and `post_params` for `GET` and
`HEAD`, then entered the read-method branch and silently discarded both. This
made successful dispatch look as if explicitly supplied data had been sent.
Falsey JSON bodies were especially easy to miss because they also looked empty
under ordinary truthiness checks.

## Design

- Treat every `body` value other than `None` as explicitly supplied.
- Reject non-empty form fields for `GET` and `HEAD`.
- Fail before header defaults, serialization, or urllib3 dispatch.
- Preserve query parameters and all write-method body behavior.

## Test First

No-network regressions covered `GET` and `HEAD` with `False`, `0`, empty text,
empty bytes, empty mappings, empty lists, and form fields. All fourteen cases
failed before implementation because the pool manager was called instead of an
`ApiValueError` being raised.

## Verification

- Run the focused request-header pytest cases.
- Run pinned `make check` from the checkout and an external directory.
- Run Python compilation and `git diff --check`.
- Require hosted Python 3.10/3.12/3.14 and CodeQL on the exact PR head.

## Scope Boundaries

- No endpoint model, authentication, URL, response, dependency, packaging,
  workflow, or live Twilio behavior change.
- Preserve this maintained transport patch during any generated-client refresh.
