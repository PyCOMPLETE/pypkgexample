# Hello From

This package provides an example of python package, including compiled parts in C and Fortran, following the standard structure for python packaging.

It illustrates how tho create a package that can be easily installed using the [Python Package Installer (pip)](https://pip.pypa.io/), which automatically retrieves all the dependencies and compiles extensions in C and Fortran. 

The package can therefore be simply done by typing:
```bash
pip install hellofrom
```
assuming that the packagee has been downloaded in the current folder.

The package performs two tasks for illustration purposes:
 - it says "hello";
 - it computes the square root of an array (to illustrate how to pass an array to Fortran or C compiled code).
 
These features are implemented in pure python, as well as through extensions implemented in Fortran (via [f2py]()) and in C (via ctypes and cython).

It works as follows:
```python
 
```

## Structure of the package

The package consists in a folder named "hellofrom" which contains the source code, the installation script and additional information, some documentation, unit tests and usage examples.

## TEMP
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
