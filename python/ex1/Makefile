.PHONY: clean lint help test install-dev install 
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean-pyc: ## remove Python file artifacts
ifeq ($(OS), Windows_NT)

else
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
endif

lint: ## check style with flake8
	flake8 eer_tools tests

test: ## run tests quickly with the default Python
	$(MAKE) -C test test


install: clean ## install the package to the active Python's site-packages
	pip install -e .

install-dev: clean ## install the package to the active Python's site-packages in editable mode with all the developer packages
	pip install -e .[dev]
