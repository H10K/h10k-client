clean:
	rm -rf dist

lint:
	pycodestyle --show-pep8 --verbose .
	pydocstyle --explain --verbose .
