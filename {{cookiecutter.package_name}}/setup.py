from setuptools import find_packages, setup

import {{ cookiecutter.package_slug }}


def long_description():
    """Provides package long_description value based on root-level README.

    Returns:
        [string] representing the package's long_description attribute.
    """
    with open('README.md', 'r') as readme:
        return readme.read()

setup(
    name='{{ cookiecutter.package_slug }}',
    description='TODO: Add short description...',
    long_description=long_description(),
    long_description_content_type='text/markdown',

    version={{ cookiecutter.package_slug }}.__version__,
    python_requires='>= {{ cookiecutter.minimum_python_version }}',

    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.author_email }}',
    url='TODO: Add project/repo URL...',

    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)
