#!/usr/bin/env python3
from pathlib import Path
import re
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
RESPONSE_LOGGING_PLAN = DOCS_PLANS / "2026-06-12-rest-response-logging.md"
CONTENT_TYPE_PLAN = DOCS_PLANS / "2026-06-12-content-type-routing.md"
EFFECTIVE_HOST_AUTH_PLAN = DOCS_PLANS / "2026-06-13-effective-host-basic-auth.md"
AUTH_MATERIALIZATION_PLAN = DOCS_PLANS / "2026-06-13-effective-host-auth-materialization.md"
ROOT_CLEANUP_PLAN = DOCS_PLANS / "2026-06-14-make-root-cleanup-protection.md"
HEADER_PRECEDENCE_PLAN = DOCS_PLANS / "2026-06-14-operation-header-precedence.md"
ARTIFACT_CHECKER = ROOT / "scripts" / "check_package_artifact.py"
REQUEST_HEADERS_TEST = ROOT / "test" / "test_rest_request_headers.py"
AUTH_CONFIGURATION_TEST = ROOT / "test" / "test_auth_configuration.py"
HEADER_PRECEDENCE_TEST = ROOT / "test" / "test_api_client_header_precedence.py"


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
    if not RESPONSE_LOGGING_PLAN.exists():
        failures.append("docs/plans/2026-06-12-rest-response-logging.md is missing")
    if not CONTENT_TYPE_PLAN.exists():
        failures.append("docs/plans/2026-06-12-content-type-routing.md is missing")
    if not EFFECTIVE_HOST_AUTH_PLAN.exists():
        failures.append("docs/plans/2026-06-13-effective-host-basic-auth.md is missing")
    if not AUTH_MATERIALIZATION_PLAN.exists():
        failures.append("docs/plans/2026-06-13-effective-host-auth-materialization.md is missing")
    if not ROOT_CLEANUP_PLAN.exists():
        failures.append("docs/plans/2026-06-14-make-root-cleanup-protection.md is missing")
    if not HEADER_PRECEDENCE_PLAN.exists():
        failures.append("docs/plans/2026-06-14-operation-header-precedence.md is missing")
    if not REQUEST_HEADERS_TEST.exists():
        failures.append("test/test_rest_request_headers.py is missing")

    plans = sorted(DOCS_PLANS.glob("*.md")) if DOCS_PLANS.exists() else []
    if not plans:
        failures.append("docs/plans must contain at least one completed plan")

    for plan_path in plans:
        plan = plan_path.read_text(encoding="utf-8")
        if "Status: Completed" not in plan or "make check" not in plan:
            failures.append(f"{plan_path.relative_to(ROOT)} must record completed status and make check verification")

    if HEADER_PRECEDENCE_PLAN.exists():
        header_plan = HEADER_PRECEDENCE_PLAN.read_text(encoding="utf-8")
        for evidence in (
            "repository and external-directory pinned `make check` passed",
            "hostile header-precedence mutations were rejected",
        ):
            if evidence not in header_plan:
                failures.append(f"{HEADER_PRECEDENCE_PLAN.relative_to(ROOT)} must record verification evidence: {evidence}")

    configuration = (ROOT / "openapi_client" / "configuration.py").read_text(encoding="utf-8")
    if "def host_allows_basic_auth(self, host=None):" not in configuration:
        failures.append("openapi_client/configuration.py must guard Basic auth by host scheme")
    if "effective_host = self.host if host is None else host" not in configuration:
        failures.append("Basic auth host checks must honor an explicit effective host")
    if 'parsed_host.scheme == "http"' not in configuration:
        failures.append("local Basic auth exceptions must be limited to plain HTTP")
    if "LOCAL_BASIC_AUTH_HOSTS" not in configuration:
        failures.append("openapi_client/configuration.py must allow explicit local Basic auth hosts")
    if "if basic_auth_token:" not in configuration:
        failures.append("Basic auth credentials must remain available for effective-host dispatch")
    if "if basic_auth_token and self.host_allows_basic_auth():" in configuration:
        failures.append("Configuration must not prefilter Basic auth using the default host")

    api_client = (ROOT / "openapi_client" / "api_client.py").read_text(encoding="utf-8")
    if "operation_headers = header_params or {}" not in api_client:
        failures.append("ApiClient must preserve the operation header mapping")
    if "header_params = dict(self.default_headers)\n        header_params.update(operation_headers)" not in api_client:
        failures.append("ApiClient defaults must be merged before operation-specific headers")
    if "header_params.update(self.default_headers)" in api_client:
        failures.append("ApiClient defaults must not overwrite operation-specific headers")
    for contract in (
        "request_host = self.configuration.host if _host is None else _host",
        "request_host=request_host",
        "auth_setting['type'] == 'basic'",
        "self.configuration.host_allows_basic_auth(",
        "url = request_host + resource_path",
    ):
        if contract not in api_client:
            failures.append(f"effective-host Basic auth contract is missing: {contract}")
    if not AUTH_CONFIGURATION_TEST.exists():
        failures.append("test/test_auth_configuration.py is missing")
    else:
        auth_test = AUTH_CONFIGURATION_TEST.read_text(encoding="utf-8")
        for contract in (
            "test_basic_auth_uses_effective_request_host",
            "test_https_override_can_authorize_when_default_host_is_disallowed",
            '("https://api.example.test", True)',
            '("http://localhost:8080", True)',
            '("http://api.example.test", False)',
            '("ftp://localhost", False)',
            'assert captured["url"] == request_host +',
        ):
            if contract not in auth_test:
                failures.append(f"effective-host Basic auth coverage is missing: {contract}")
    documentation_contracts = {
        "README.md": "operation-level host overrides",
        "SECURITY.md": "effective request host",
        "VISION.md": "operation-level host overrides",
    }
    for relative_path, contract in documentation_contracts.items():
        if contract not in (ROOT / relative_path).read_text(encoding="utf-8"):
            failures.append(
                f"{relative_path} must document the effective-host Basic auth guard"
            )
    for relative_path in ("README.md", "SECURITY.md", "VISION.md", "CHANGES.md"):
        if "dispatch-time host" not in (ROOT / relative_path).read_text(encoding="utf-8"):
            failures.append(f"{relative_path} must document dispatch-time host authorization")

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
    if "def _resolve_content_type(headers):" not in rest:
        failures.append("REST requests must resolve Content-Type in a helper")
    if "key.lower() == 'content-type'" not in rest:
        failures.append("REST Content-Type lookup must be case-insensitive")
    if "value.split(';', 1)[0].strip().lower()" not in rest:
        failures.append("REST Content-Type routing must use the normalized base media type")
    if "del headers[content_type_header]" not in rest:
        failures.append("multipart routing must remove the resolved Content-Type spelling")
    if "multiple Content-Type values" not in rest:
        failures.append("REST requests must reject ambiguous Content-Type variants")
    request_headers_test = (
        REQUEST_HEADERS_TEST.read_text(encoding="utf-8")
        if REQUEST_HEADERS_TEST.exists()
        else ""
    )
    for test_name in (
        "test_parameterized_json_content_type_uses_json_body_without_duplicate_header",
        "test_lowercase_parameterized_form_content_type_uses_form_fields",
        "test_lowercase_parameterized_multipart_header_is_removed_from_copy",
        "test_duplicate_content_type_case_variants_fail_before_transport",
    ):
        if f"def {test_name}():" not in request_headers_test:
            failures.append(f"REST Content-Type coverage is missing: {test_name}")
    if 'logger.debug("response body: %s", r.data)' in rest:
        failures.append("REST debug logging must not emit response bodies")
    if '"response received: status=%s bytes=%s"' not in rest:
        failures.append("REST debug logging must retain response status and size metadata")

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

    response_logging_tests = ROOT / "test" / "test_rest_response_logging.py"
    if not response_logging_tests.exists():
        failures.append("test/test_rest_response_logging.py is missing")
    else:
        response_logging_test_text = response_logging_tests.read_text(encoding="utf-8")
        for contract in [
            "test_success_response_logs_metadata_without_body",
            "test_error_response_logs_metadata_without_body",
            'caplog.set_level(logging.DEBUG, logger="openapi_client.rest")',
            "assert response.data == body",
            "assert captured.value.body == body",
        ]:
            if contract not in response_logging_test_text:
                failures.append(f"REST response logging regression contract is missing: {contract}")
        if response_logging_test_text.count('assert "super-secret" not in caplog.text') != 2:
            failures.append("REST response logging tests must protect both response paths from payload disclosure")

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
    root_declaration = "override ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))"
    root_assignments = re.findall(r"^(?:override\s+)?ROOT\s*[:+?]?=", makefile, re.MULTILINE)
    if len(root_assignments) != 1 or makefile.count(root_declaration) != 1:
        failures.append("Makefile must contain exactly one protected repository-root declaration")
    if makefile.count(root_declaration + "\nPYTHON ?= python3") != 1:
        failures.append("Makefile must keep the protected root before the Python override")
    for contract in (
        ".PHONY: build check lint package-smoke test verify",
        "build: lint",
        "package-smoke: build",
        "verify: lint test package-smoke",
        "check: verify",
        'rm -rf "$(ROOT)/build" "$(ROOT)/dist" "$(ROOT)"/*.egg-info',
        '$(PYTHON) -m build --no-isolation --outdir "$(ROOT)/dist" "$(ROOT)"',
        'scripts/check_package_artifact.py',
        "env -u PYTHONPATH $(PYTHON) -m pip check",
        'pip_audit -r "$(ROOT)/requirements.txt"',
    ):
        if contract not in makefile:
            failures.append(f"Makefile verification contract is missing: {contract}")

    if "docs/plans/2026-06-14-make-root-cleanup-protection.md" not in (ROOT / "README.md").read_text(encoding="utf-8"):
        failures.append("README must index Make root cleanup protection evidence")
    if "docs/plans/2026-06-14-operation-header-precedence.md" not in (ROOT / "README.md").read_text(encoding="utf-8"):
        failures.append("README must index operation header precedence evidence")

    if not HEADER_PRECEDENCE_TEST.exists():
        failures.append("test/test_api_client_header_precedence.py is missing")
    else:
        header_test = HEADER_PRECEDENCE_TEST.read_text(encoding="utf-8")
        for contract in (
            "test_operation_headers_override_defaults_without_mutating_input",
            'client.set_default_header("Content-Type", "application/json")',
            '"Content-Type": "application/x-www-form-urlencoded"',
            'assert captured["headers"]["Content-Type"] == "application/x-www-form-urlencoded"',
            'assert captured["headers"]["X-Default"] == "default-value"',
            "assert operation_headers == original_headers",
        ):
            if contract not in header_test:
                failures.append(f"operation header precedence coverage is missing: {contract}")

    for relative_path in ("README.md", "SECURITY.md", "VISION.md", "CHANGES.md"):
        if "operation header precedence" not in (ROOT / relative_path).read_text(encoding="utf-8").lower():
            failures.append(f"{relative_path} must document operation header precedence")

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
