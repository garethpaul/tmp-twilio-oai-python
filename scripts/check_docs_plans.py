#!/usr/bin/env python3
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS_PLANS = ROOT / "docs" / "plans"
CANONICAL_PLAN = DOCS_PLANS / "2026-06-08-tmp-twilio-oai-python-baseline.md"
QUERY_APPEND_PLAN = DOCS_PLANS / "2026-06-09-write-query-append.md"
REPEATED_QUERY_PLAN = DOCS_PLANS / "2026-06-09-repeated-write-query-params.md"


def main():
    failures = []

    if not CANONICAL_PLAN.exists():
        failures.append("docs/plans/2026-06-08-tmp-twilio-oai-python-baseline.md is missing")
    if not QUERY_APPEND_PLAN.exists():
        failures.append("docs/plans/2026-06-09-write-query-append.md is missing")
    if not REPEATED_QUERY_PLAN.exists():
        failures.append("docs/plans/2026-06-09-repeated-write-query-params.md is missing")

    plans = sorted(DOCS_PLANS.glob("*.md")) if DOCS_PLANS.exists() else []
    if not plans:
        failures.append("docs/plans must contain at least one completed plan")

    for plan_path in plans:
        plan = plan_path.read_text(encoding="utf-8")
        if "Status: Completed" not in plan or "make check" not in plan:
            failures.append(f"{plan_path.relative_to(ROOT)} must record completed status and make check verification")

    configuration = (ROOT / "openapi_client" / "configuration.py").read_text(encoding="utf-8")
    if "def host_allows_basic_auth(self):" not in configuration:
        failures.append("openapi_client/configuration.py must guard Basic auth by host scheme")
    if "LOCAL_BASIC_AUTH_HOSTS" not in configuration:
        failures.append("openapi_client/configuration.py must allow explicit local Basic auth hosts")

    rest = (ROOT / "openapi_client" / "rest.py").read_text(encoding="utf-8")
    if "headers = dict(headers or {})" not in rest:
        failures.append("openapi_client/rest.py must copy caller headers before mutation")
    if "def _append_query_params(url, query_params):" not in rest:
        failures.append("openapi_client/rest.py must keep query appending in a helper")
    if "urlencode(query_params, doseq=True)" not in rest:
        failures.append("openapi_client/rest.py must preserve repeated write query parameters")
    if "url = _append_query_params(url, query_params)" not in rest:
        failures.append("write requests must append query parameters without duplicating '?'")

    if failures:
        print("Documentation plan checks failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("Documentation plan checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
