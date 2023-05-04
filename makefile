PYTHON = poetry run

## @ pre-commit
.PHONY: pre-commit
pre-commit:
	${PYTHON} black --check .
	${PYTHON} isort --check .

## @ format
.PHONY: format
format:
	${PYTHON} black  .
	${PYTHON} isort  .

## @ test
.PHONY: test
test:
	${PYTHON} pytest -v