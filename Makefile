.PHONY: requirements requirements_tools requirements_test lint test

TEST_PATH=./tests

requirements:
	poetry install --no-dev

requirements_test:
	poetry install 

lint: requirements_tools
	poetry run flake8 --exclude=env,venv

test: requirements_test
ifndef TEST_ONLY
	TEST_ONLY=$(TEST_PATH)
endif
	poetry run  pytest -s -vv --color=yes $(TEST_ONLY)
