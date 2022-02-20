install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3.10 -m pip install --user ~/Desktop/tasks/ruvents_test_task/dist/*.whl
package-reinstall:
	python3.10 -m pip install --user ~/Desktop/tasks/ruvents_test_task/dist/*.whl --force-reinstall

all: build publish package-reinstall

lint:
	poetry run flake8 xls_handler
test:
	poetry run pytest -vv
sort:
	poetry run isort .