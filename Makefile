.PHONY: build check lint package-smoke test verify

override ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
PYTHON ?= python3

lint:
	$(PYTHON) -m py_compile \
		"$(ROOT)/setup.py" \
		"$(ROOT)/openapi_client/configuration.py" \
		"$(ROOT)/openapi_client/api_client.py" \
		"$(ROOT)/openapi_client/rest.py" \
		"$(ROOT)/scripts/check_package_artifact.py"
	$(PYTHON) "$(ROOT)/scripts/check_docs_plans.py"

test:
	cd "$(ROOT)" && $(PYTHON) -m pytest -q

build: lint
	rm -rf "$(ROOT)/build" "$(ROOT)/dist" "$(ROOT)"/*.egg-info
	$(PYTHON) -m build --no-isolation --outdir "$(ROOT)/dist" "$(ROOT)"

package-smoke: build
	$(PYTHON) "$(ROOT)/scripts/check_package_artifact.py"

verify: lint test package-smoke

check: verify
	env -u PYTHONPATH $(PYTHON) -m pip check
	env -u PYTHONPATH $(PYTHON) -m pip_audit -r "$(ROOT)/requirements.txt"
