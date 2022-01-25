.PHONY: test lint

help:	## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

compile-requirements:	## Compile requirements with fixed version
	@python -m pip install pip-tools
	@pip-compile requirements\requirements.in --output-file requirements.txt
	@pip-compile requirements\dev-requirements.in --output-file dev-requirements.txt

lint:	## Linting
	@echo "Lint"
	@python -m black --check .
	@python -m flake8
	@python -m bandit -c bandit.yaml .

test:	## Run the tests
	@echo "Tests"
	PYTHONPATH=. python -m pytest --cov=./ --cov-report=xml