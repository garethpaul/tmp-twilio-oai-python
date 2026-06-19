---
title: Response Body Size Limit
type: security
status: completed
date: 2026-06-16
---

# Response Body Size Limit

## Status: Completed

## Problem Frame

Normal generated-client requests pass `preload_content=True` directly to
urllib3. urllib3 therefore reads and decodes the complete response before the
client can inspect its size, allowing an unexpectedly large or highly
compressed response to consume unbounded process memory.

## Priorities

1. P0: Bound decoded response bytes before they are accumulated in memory.
2. P1: Close an oversized or failed response without returning its connection
   to the pool as reusable.
3. P2: Preserve successful response data, status handling, and explicit
   `_preload_content=False` streaming behavior.

## Scope Boundaries

- Add a configurable positive response-body byte limit with a 5 MiB default.
- Read preloaded responses through urllib3's bounded decoded-read interface.
- Reject oversized declared and actual decoded bodies with `ApiException`.
- Add captured-response regressions and static package-gate contracts.
- Update maintained guidance and changelog notes.
- Do not change request bodies, authentication, redirects, endpoint models,
  pagination, timeouts, dependencies, or caller-managed streaming responses.
- Do not claim live Twilio API execution or credential validation.

## Implementation Units

### U1: Configuration Boundary

Expose the response-body limit on `Configuration`, validate it before transport
dispatch, and reject booleans, non-integers, and non-positive values.

### U2: Bounded Preloading

Ask urllib3 not to preload ordinary responses, fail early when a valid
`Content-Length` exceeds the configured limit, then read at most one decoded
byte beyond the limit. Preserve accepted bytes in `RESTResponse`; close the
transport response on oversize or read failure and release a fully consumed
accepted response normally. Leave explicit streaming responses untouched.

### U3: Mutation-Sensitive Verification

Add focused tests for the default and custom limits, exact-boundary success,
declared and decoded oversize rejection, transport cleanup, error-response
handling, and streaming pass-through. Extend the maintained gate so removing
the configuration, bounded read, cleanup, tests, guidance, or completed plan
causes verification to fail.

## Verification Plan

- Prove focused limit regressions fail before the implementation.
- Run focused tests and the full pinned `make check` with explicit timeouts.
- Run the full pinned gate from the repository root and an external directory.
- Reject isolated configuration, validation, bounded-read, cleanup, streaming,
  test, guidance, and completed-plan mutations.
- Audit exact intended paths, generated artifacts, dependency/vendor drift,
  whitespace, conflict markers, and credential-shaped additions.

## Work Completed

- Added a configurable positive decoded response limit with a 5 MiB default.
- Moved ordinary responses to client-managed bounded preloading while preserving
  explicit caller-managed streaming.
- Closed declared, decoded, or failed oversized transports; released accepted
  responses; and preserved bounded non-2xx response bodies.
- Added real gzip and captured-response regressions, static contracts,
  synchronized guidance, and completed-plan enforcement.

## Verification Completed

- All 401 pinned offline tests passed, including 17 focused response-body-limit
  cases and a real urllib3 gzip decoding case.
- The repository and external-directory pinned `make check` passed against the
  actual worktree, including source/wheel builds, isolated wheel import,
  dependency consistency, and auditing with no known vulnerabilities.
- Ten isolated hostile response-body-limit mutations were rejected across
  configuration, validation, bounded reads, close/release behavior, urllib3
  preloading, streaming, tests, guidance, and plan status.
- No live Twilio request, credential, account data, or unbounded payload was
  used.
