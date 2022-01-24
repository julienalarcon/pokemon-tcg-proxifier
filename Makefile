.PHONY: test lint

help:	## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

lint:	## Linting
	@echo "Lint"
	@python -m black --check .
	@python -m flake8
	@python -m bandit -c bandit.yaml .

test:	## Run the tests
	@echo "Tests"
	PYTHONPATH=. python -m pytest