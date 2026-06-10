.PHONY: build check lint test verify

PYTHON ?= python3

lint:
	$(PYTHON) -m py_compile setup.py openapi_client/configuration.py openapi_client/api_client.py openapi_client/rest.py
	$(PYTHON) scripts/check_docs_plans.py

test:
	$(PYTHON) -m pytest -q

build: lint
	rm -rf build dist *.egg-info
	$(PYTHON) -m build --no-isolation

verify: lint test build

check: verify
	$(PYTHON) -m pip_audit --local
