# Error Response Charset Decoding

Status: Completed

## Context

Successful text responses already honored a declared `Content-Type` charset,
but byte-backed `ApiException` bodies were always decoded as UTF-8. A provider
error encoded as ISO-8859-1 therefore replaced valid non-ASCII characters and
gave callers corrupted diagnostic text.

## Design

Read `Content-Type` from exception headers case-insensitively and reuse the
existing response charset parser and replacement decoder. Keep UTF-8 with
replacement as the fallback when headers are absent or the declared codec is
unknown. Preserve the original exception instance, status, reason, and headers.

## Verification

- An ISO-8859-1 error body decodes `café` without replacement characters.
- An unknown error charset falls back to UTF-8 replacement without raising.
- Existing missing-header UTF-8 exception behavior remains unchanged.
- `make check` runs the full source, test, build, audit, and wheel smoke gates.
