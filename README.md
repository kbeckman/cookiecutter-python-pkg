# cookiecutter-python-pkg

This project is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) project / repository template for
creating a Python package. Unlike most things in the Python universe, this project is opinionated and utilizes, in my
opinion, the best-of-breed utilities and tooling for the job. As my opinions change, this project will change too.
Feedback is welcomed.


## Environment Setup

### Prerequisites

```shell
brew install cookiecutter
```
_For non-macOS installations, refer to the_
_[installation documentation](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html#install-cookiecutter)._


## Usage

```shell
# cookiecutter will prompt you for necessary project variable values...
cookiecutter path/to/cookiecutter-python-pkg
```

### cookiecutter Varialbes

| Variable                      | Description                                                     | Calculated        |
| -------                       | -----------                                                     | -------           |
| **package_name**              | Python package name (can include '-')                           | no, user provided |
| **package_slug**              | Python **package_name** as _snake_case_.                        | _[calculated]_    |
| **asdf_python_version**       | Python version to use as ASDF project Python.                   | no, user provided |
| **minimum_python_version**    | Minimum supported Python version from **asdf_python_version**.  | _[calculated]_    |
| **author**                    | Package author's full name.                                     | no, user provided |
| **author_email**              | Package author's email address.                                 | no, user provided |


## Additional Resources

* [Cookiecutter Documentation](https://cookiecutter.readthedocs.io)
* [Jinja Template Documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/#)
