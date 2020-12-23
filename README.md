# pypkgexample

This package provides an example of python package, including compiled parts in C and Fortran, following the standard structure for python packaging.

It illustrates how tho create a package that can be easily installed using the [Python Package Installer (pip)](https://pip.pypa.io/), which automatically retrieves all the dependencies and compiles extensions in C and Fortran. 

The package can therefore be simply done by typing:
```bash
pip install pypkgexample
```
assuming that the packagee has been downloaded in the current folder.

## Example code

The package performs two tasks for illustration purposes:
 - it says "hello";
 - it computes the square root of an array (to illustrate how to pass an array to Fortran or C compiled code).
 
These features are implemented in pure python, as well as through extensions implemented in Fortran (bound via [f2py](https://numpy.org/doc/stable/f2py/)) and in C (bound via [ctypes](https://docs.python.org/3/library/ctypes.html) and [cython](https://cython.org)).

The package can be used as follows:
```python
import pypkgexample as pe

pe.say_hello_python()
pe.say_hello_fortran()
pe.say_hello_c_ctypes()
pe.say_hello_c_cython()

# produces the following output:
#
# Hello from python!
#  Hello from Fortran!
# Hello from C with ctypes!
# Hello from C with cython!
```

```python
import numpy as np
import pypkgexample as pe

a = np.array([9., 4., 1.])

print(f'From python: {pe.sqrt_array_python(a)}')
print(f'From Fortran via f2py: {pe.sqrt_array_fortran(a)}')
print(f'From C via ctypes: {pe.sqrt_array_c_ctypes(a)}')
print(f'From C via cython: {pe.sqrt_array_c_cython(a)}')

# produces the following output:
#
# From python: [3., 2., 1.]
# From Fortran: [3., 2., 1.]
# From C with ctypes: [3., 2., 1.]
# From C with cython: [3., 2., 1.]
```

## Structure of the package

```pypkgexample``` has the structure used for standard python packages. It consists in a folder named after the package "pypkgexample" (which is also the top level of the git repository) that contains the source code, the code and information for the installation, documentation, unit tests and usage examples. In particular:
 - The **source code** is hosted in a subfolder that also has the same name of the python package (pypkgexample).


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
