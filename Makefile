.DEFAULT_GOAL := check
.PHONY: __repository-make-authority build check lint package-smoke root-test test verify
.SECONDEXPANSION:

PYTHON ?= python3
override PYTHON := $(value PYTHON)
export PYTHON
override SHELL := /bin/sh
override .SHELLFLAGS := -c

ifneq ($(filter command line,$(origin MAKEFLAGS)),)
$(error MAKEFLAGS must not be overridden for repository verification)
endif
override REPOSITORY_MAKE_FIRST_FLAGS := $(firstword $(MAKEFLAGS))
ifneq ($(filter -%,$(REPOSITORY_MAKE_FIRST_FLAGS)),)
override REPOSITORY_MAKE_FIRST_FLAGS :=
endif
override REPOSITORY_MAKE_SHORT_FLAGS := $(REPOSITORY_MAKE_FIRST_FLAGS) $(filter-out --%,$(filter -%,$(MAKEFLAGS)))
ifneq ($(findstring n,$(REPOSITORY_MAKE_SHORT_FLAGS)),)
$(error non-executing or error-ignoring MAKEFLAGS are not supported for repository verification)
endif
ifneq ($(findstring t,$(REPOSITORY_MAKE_SHORT_FLAGS)),)
$(error non-executing or error-ignoring MAKEFLAGS are not supported for repository verification)
endif
ifneq ($(findstring q,$(REPOSITORY_MAKE_SHORT_FLAGS)),)
$(error non-executing or error-ignoring MAKEFLAGS are not supported for repository verification)
endif
ifneq ($(findstring i,$(REPOSITORY_MAKE_SHORT_FLAGS)),)
$(error non-executing or error-ignoring MAKEFLAGS are not supported for repository verification)
endif
ifneq ($(filter --just-print --dry-run --recon --touch --question --ignore-errors,$(MAKEFLAGS)),)
$(error non-executing or error-ignoring MAKEFLAGS are not supported for repository verification)
endif
ifneq ($(strip $(MAKEFILES)),)
$(error MAKEFILES must be empty; repository verification requires this Makefile to be loaded alone)
endif
override MAKEFILES :=
ifneq ($(origin MAKEFILE_LIST),file)
$(error MAKEFILE_LIST must not be overridden)
endif
override ROOT := $(shell path='$(subst ','"'"',$(value MAKEFILE_LIST))'; path=$$(printf '%s' "$$path" | /usr/bin/sed 's/^ //'); [ -f "$$path" ] || exit 1; directory=$$(/usr/bin/dirname -- "$$path"); CDPATH= cd -- "$$directory" && /bin/pwd -P)
export ROOT
ifeq ($(strip $(ROOT)),)
$(error repository Makefile path could not be resolved)
endif

build check lint package-smoke root-test test verify: $$(if $$(filter file,$$(origin MAKEFILE_LIST)),,$$(error MAKEFILE_LIST must not be overridden))
build check lint package-smoke root-test test verify: $$(if $$(shell path=$$$$(/usr/bin/printf '%s' '$$(subst ','"'"',$$(MAKEFILE_LIST))' | /usr/bin/sed 's/^ //') && [ -f "$$$$path" ] && /usr/bin/printf '%s' ok),,$$(error repository Makefile must be loaded alone))
build check lint package-smoke root-test test verify: __repository-make-authority

__repository-make-authority::
	@:

lint:
	"$$PYTHON" -m py_compile \
		"$$ROOT/setup.py" \
		"$$ROOT/openapi_client/configuration.py" \
		"$$ROOT/openapi_client/api_client.py" \
		"$$ROOT/openapi_client/rest.py" \
		"$$ROOT/scripts/check_package_artifact.py"
	"$$PYTHON" "$$ROOT/scripts/check_docs_plans.py"

test:
	cd "$$ROOT" && "$$PYTHON" -m pytest -q

build: lint
	/bin/rm -rf -- "$$ROOT/build" "$$ROOT/dist" "$$ROOT"/*.egg-info
	"$$PYTHON" -m build --no-isolation --outdir "$$ROOT/dist" "$$ROOT"

package-smoke: build
	"$$PYTHON" "$$ROOT/scripts/check_package_artifact.py"

root-test:
	/bin/sh "$$ROOT/scripts/test-makefile-root.sh"

verify: root-test lint test package-smoke

check: verify
	env -u PYTHONPATH "$$PYTHON" -m pip check
	env -u PYTHONPATH "$$PYTHON" -m pip_audit -r "$$ROOT/requirements.txt"
