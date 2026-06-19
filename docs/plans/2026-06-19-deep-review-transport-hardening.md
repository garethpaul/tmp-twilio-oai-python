# Deep Review Transport Hardening

Status: Completed

## Problem

The chained generated-client pull requests improved request and response safety,
but hostile no-network review found remaining boundary failures: Basic auth was
still accepted for any HTTPS override, caller-controlled header controls reached
the transport, custom retry policies could retain sensitive headers on redirects,
media types containing `json` were treated as JSON, valid quoted or underscore
charsets were ignored, and non-preloaded error responses could read or retain an
unbounded transport body while raising.

## Requirements

- Bind Basic auth to the configured origin, not merely a secure-looking scheme.
- Strip Authorization, Cookie, and Proxy-Authorization on cross-host redirects
  even when callers supply a permissive urllib3 `Retry` policy.
- Reject invalid request URLs, URL userinfo, header names, and header control
  characters before transport dispatch.
- Serialize mappings as JSON only for `application/json` and structured `+json`
  media types.
- Parse valid quoted and underscore charset names and retain UTF-8 replacement
  fallback for unknown charsets.
- Close streaming error responses without reading their body; successful
  streaming remains caller-managed and intentionally unbounded.
- Preserve generated public API signatures and avoid live Twilio credentials or
  requests.

## Evidence

- Focused hostile fake-HTTP regressions cover cross-origin auth, header controls,
  URL userinfo, JSON routing, redirect policy, charset parsing, and streaming
  error cleanup.
- Existing decoded response-limit tests cover declared, chunked, and compressed
  oversized bodies.
- Mutation runs proved the focused tests fail when origin binding, header
  validation, strict JSON routing, response limits, or streaming cleanup are
  removed.
- `make check`, package build/smoke, dependency audit, and hosted Python gates
  passed after consolidation.

## Residual risk

No live Twilio request was sent and no real credential was used. Offline fake
transport coverage cannot prove service-specific redirects, proxy behavior, or
production response shapes. Explicit successful streaming remains caller-owned
and bypasses the preload limit by design.
