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
	coverage run ./h10kcli/__init__.py -l -f ./h10kcli/tests/configs/h10k.yml
	coverage report --show-missing
