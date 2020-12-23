# Hello From

This package provides an example of python package, including compiled parts in C and Fortran, following the standard structure for python packaging.

It illustrates how tho create a package that can be easily installed using the [Python Package Installer (pip)](https://pip.pypa.io/), which automatically retrieves all the dependences and compiles extensions in C and Fortran. This can be simply done by typing:
```bash
pip install hellofrom
```
assuming that the project has been downloaded in the current folder or made availabe in the [Python Package Index PyPI](https://pypi.org).


Following PEP517, the setup is not executed by your python environment, but by an environment built ad-hoc at install time.
The packages to be retrieved for the installation are specified in pyproject.toml. Note that numpy needs to be included in order to compile extensions with f2py.

```toml
[build-system]
build-backend = 'setuptools.build_meta'
requires = [
    'setuptools >= 43.0.0',
    'numpy'
]
```
