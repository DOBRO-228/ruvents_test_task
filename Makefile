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
	poetry run flake8 page_loader
test:
	poetry run pytest -vv
test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml
sort:
	poetry run isort .