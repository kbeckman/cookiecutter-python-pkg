default: project.ci


# (One-Time) Sets up the project Python virtual environment...
.PHONY: project.setup
project.setup:
	pip install --upgrade pip pipenv setuptools wheel
	pipenv install --dev


# Cleans package build artifacts, development logs, etc...
.PHONY: package.clean
project.clean:
	rm -rf build
	rm -rf dist
	rm -rf ./**/*.egg-info


# Runs all CI-related build commands...
.PHONY: project.ci
project.ci: project.pylint project.pytest


# Runs PyLint...
.PHONY: project.pylint
project.pylint:
	pipenv run pylint setup.py src/{{ cookiecutter.package_slug }}/* test/*


# Runs PyTest...
.PHONY: project.pytest
project.pytest:
	pipenv run pytest


# Builds the python package for deployment / installation...
.PHONY: package.build
package.build:
	python setup.py sdist bdist_wheel
