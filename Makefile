.PHONY: build check lint test verify

PYTHON ?= python3

lint:
	$(PYTHON) -m py_compile setup.py openapi_client/configuration.py openapi_client/api_client.py

test:
	$(PYTHON) -m pytest -q

build: lint
	$(PYTHON) setup.py check

verify: lint test build

check: verify
