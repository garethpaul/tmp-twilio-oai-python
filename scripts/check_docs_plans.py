#!/usr/bin/env python3
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS_PLANS = ROOT / "docs" / "plans"
CANONICAL_PLAN = DOCS_PLANS / "2026-06-08-tmp-twilio-oai-python-baseline.md"
QUERY_APPEND_PLAN = DOCS_PLANS / "2026-06-09-write-query-append.md"
REPEATED_QUERY_PLAN = DOCS_PLANS / "2026-06-09-repeated-write-query-params.md"
UNSUPPORTED_METHOD_PLAN = DOCS_PLANS / "2026-06-09-unsupported-rest-method.md"
MODERNIZATION_PLAN = DOCS_PLANS / "2026-06-10-python-package-and-ci-modernization.md"
ARTIFACT_PLAN = DOCS_PLANS / "2026-06-10-wheel-artifact-verification.md"
TRANSPORT_PLAN = DOCS_PLANS / "2026-06-10-rest-transport-errors.md"
TIMEOUT_PLAN = DOCS_PLANS / "2026-06-12-rest-timeout-validation.md"
ARTIFACT_CHECKER = ROOT / "scripts" / "check_package_artifact.py"


def main():
    failures = []

    if not CANONICAL_PLAN.exists():
        failures.append("docs/plans/2026-06-08-tmp-twilio-oai-python-baseline.md is missing")
    if not QUERY_APPEND_PLAN.exists():
        failures.append("docs/plans/2026-06-09-write-query-append.md is missing")
    if not REPEATED_QUERY_PLAN.exists():
        failures.append("docs/plans/2026-06-09-repeated-write-query-params.md is missing")
    if not UNSUPPORTED_METHOD_PLAN.exists():
        failures.append("docs/plans/2026-06-09-unsupported-rest-method.md is missing")
    if not MODERNIZATION_PLAN.exists():
        failures.append("docs/plans/2026-06-10-python-package-and-ci-modernization.md is missing")
    if not ARTIFACT_PLAN.exists():
        failures.append("docs/plans/2026-06-10-wheel-artifact-verification.md is missing")
    if not TRANSPORT_PLAN.exists():
        failures.append("docs/plans/2026-06-10-rest-transport-errors.md is missing")
    if not TIMEOUT_PLAN.exists():
        failures.append("docs/plans/2026-06-12-rest-timeout-validation.md is missing")

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
    if "assert method in" in rest:
        failures.append("openapi_client/rest.py must not rely on optimized-away assert statements for method validation")
    if "allowed_methods = {" not in rest or "if method not in allowed_methods:" not in rest:
        failures.append("openapi_client/rest.py must explicitly validate supported HTTP methods")
    if "Unsupported HTTP method" not in rest:
        failures.append("openapi_client/rest.py must raise a clear unsupported-method error")
    if "except urllib3.exceptions.HTTPError as e:" not in rest:
        failures.append("openapi_client/rest.py must normalize urllib3 transport errors")
    if rest.count("raise ApiException(status=0, reason=msg) from e") < 2:
        failures.append("REST transport wrappers must preserve their urllib3 exception cause")
    if "def _prepare_request_timeout(value):" not in rest:
        failures.append("openapi_client/rest.py must validate request timeouts in a helper")
    if "not math.isfinite(component)" not in rest:
        failures.append("REST timeout validation must reject non-finite values")
    if "timeout = _prepare_request_timeout(_request_timeout)" not in rest:
        failures.append("REST requests must validate timeouts before transport dispatch")

    timeout_tests = ROOT / "test" / "test_rest_request_timeout.py"
    if not timeout_tests.exists():
        failures.append("test/test_rest_request_timeout.py is missing")
    else:
        timeout_test_text = timeout_tests.read_text(encoding="utf-8")
        for contract in [
            "test_request_preserves_default_timeout_when_omitted",
            "test_request_accepts_positive_total_timeout",
            "test_request_accepts_connect_read_timeout_tuple",
            "test_request_rejects_invalid_timeout_before_pool_request",
            "assert client.pool_manager.calls == []",
        ]:
            if contract not in timeout_test_text:
                failures.append(f"REST timeout regression contract is missing: {contract}")

    required_files = [
        "pyproject.toml",
        "requirements-dev.txt",
        ".github/workflows/check.yml",
    ]
    for required_file in required_files:
        if not (ROOT / required_file).exists():
            failures.append(f"{required_file} is missing")

    if not ARTIFACT_CHECKER.exists():
        failures.append("scripts/check_package_artifact.py is missing")
    else:
        artifact_checker = ARTIFACT_CHECKER.read_text(encoding="utf-8")
        for contract in (
            "if len(WHEELS) != 1:",
            '"--target",',
            'environment.pop("PYTHONPATH", None)',
            '[sys.executable, "-I", "-c", smoke_test]',
            ".is_relative_to(target)",
        ):
            if contract not in artifact_checker:
                failures.append(f"package artifact checker is missing: {contract}")

    for obsolete_ci in (".travis.yml", ".gitlab-ci.yml"):
        if (ROOT / obsolete_ci).exists():
            failures.append(f"{obsolete_ci} must not advertise unsupported Python runtimes")

    setup = (ROOT / "setup.py").read_text(encoding="utf-8")
    if 'python_requires=">=3.10"' not in setup:
        failures.append("setup.py must require maintained Python 3.10 or newer")
    for dependency in (
        '"urllib3 >= 2.6.3, < 3"',
        '"python-dateutil >= 2.9.0.post0, < 3"',
        '"nulltype >= 2.3.1, < 3"',
    ):
        if dependency not in setup:
            failures.append(f"setup.py dependency contract is missing: {dependency}")

    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    for contract in (
        'requires = ["setuptools==82.0.1", "wheel==0.47.0"]',
        'build-backend = "setuptools.build_meta"',
    ):
        if contract not in pyproject:
            failures.append(f"pyproject.toml build contract is missing: {contract}")

    runtime_requirements = (ROOT / "requirements.txt").read_text(encoding="utf-8")
    for dependency in (
        "nulltype==2.3.1",
        "python-dateutil==2.9.0.post0",
        "urllib3==2.7.0",
    ):
        if dependency not in runtime_requirements:
            failures.append(f"runtime requirement is missing: {dependency}")

    development_requirements = (ROOT / "requirements-dev.txt").read_text(encoding="utf-8")
    if "pip==26.1.2" not in development_requirements:
        failures.append("requirements-dev.txt must pin the audited pip version")

    makefile = (ROOT / "Makefile").read_text(encoding="utf-8")
    for contract in (
        "ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))",
        'scripts/check_package_artifact.py',
        "env -u PYTHONPATH $(PYTHON) -m pip check",
        'pip_audit -r "$(ROOT)/requirements.txt"',
    ):
        if contract not in makefile:
            failures.append(f"Makefile verification contract is missing: {contract}")

    workflow = (ROOT / ".github" / "workflows" / "check.yml").read_text(encoding="utf-8")
    workflow_contracts = [
        "permissions:\n  contents: read",
        "workflow_dispatch:",
        "concurrency:",
        "cancel-in-progress: true",
        "runs-on: ubuntu-24.04",
        "timeout-minutes: 15",
        "python-version: ['3.10', '3.12', '3.14']",
        "fail-fast: false",
        "actions/checkout@df4cb1c069e1874edd31b4311f1884172cec0e10 # v6.0.3",
        "actions/setup-python@a309ff8b426b58ec0e2a45f0f869d46889d02405 # v6.2.0",
        "run: make check",
    ]
    for contract in workflow_contracts:
        if contract not in workflow:
            failures.append(f"GitHub Actions workflow contract is missing: {contract}")

    if failures:
        print("Documentation plan checks failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("Documentation plan checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
