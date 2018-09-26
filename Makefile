PYTHON_FILES = .

all: clean lint build test

clean:
	rm -rf \
	  .coverage \
	  .eggs \
	  MANIFEST \
	  build \
	  dist \
	  h10k_client.egg-info

lint:
	pycodestyle --show-pep8 --verbose $(PYTHON_FILES)
	pydocstyle --explain --verbose $(PYTHON_FILES)

build:
	python setup.py sdist

test:
	coverage run setup.py test
	coverage run ./h10kcli/__init__.py lint -f ./h10kcli/tests/configs/h10k.yml
	coverage run ./h10kcli/__init__.py create -f ./h10kcli/tests/configs/h10k.yml -w https://foobar.h10k.io -t apitoken || true
	coverage run ./h10kcli/__init__.py delete -f ./h10kcli/tests/configs/h10k.yml -w https://foobar.h10k.io -t apitoken || true
	coverage run ./h10kcli/__init__.py status -f ./h10kcli/tests/configs/h10k.yml -w https://foobar.h10k.io -t apitoken || true
	coverage run ./h10kcli/__init__.py status -f ./h10kcli/tests/configs/h10k.yml -w https://api.h10k.io/404 -t apitoken || true
	coverage report --show-missing
