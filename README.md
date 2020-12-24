# pypkgexample

## Table of contents
 - [Introduction](#introduction) 
 - [Tasks performed by pypkgexample](#tasks-performed-by-pypkgexample)
 - [Structure of the package](#structure-of-the-package)
 - [Installation code](#installation-code)
 - [References](#references)

## Introduction
"pypkgexample" provides an example of python package including compiled parts in C and Fortran, following the standard structure for python packaging.

It illustrates how tho create a package that can be easily installed using the [Python Package Installer (pip)](https://pip.pypa.io/), which automatically retrieves all the dependencies and compiles extensions in C and Fortran. 

The package can therefore be simply installed by typing:
```bash
pip install pypkgexample
```
assuming that the package has been downloaded in the current folder.

## Tasks performed by pypkgexample

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
 - **Unit tests** are hosted in the folder "tests" and can be executed using [pytest](http://pytest.org)
 - **Examples** illustrating the package usage are hosted in the folder "examples"
 - **License** information is contained in the file "LICENSE.txt"
 - This **documentation** is contained in the file "README.md"
 - The **installation code and information** is defined by the files "pyprojet.toml", "MANIFEST.in", "setup.py", which will be described in more detail in the following section.
 
## Installation code

The build and installation process is performed by the pip pacakge installer based on the following files

### pyproject.toml

The file "pyproject.toml" defines the backend used of the build, which in our case is [setuptools](https://pypi.org/project/setuptools/), and the dependencies that are required to build the package. 
Such dependencies are not permanently installed, but are used only to build the package.

```toml
[build-system]
build-backend = 'setuptools.build_meta'
requires = [
    'setuptools >= 43.0.0',
    'numpy', # required to compile f2py extension
    'cython', # requred to compile cython extension
    ]
```

### MANIFEST.in

The file "MANIFEST.in" defined the additional files that need to be copied together with the installed packeage together with those that are strictly required for the package to work. In our case we include this readme file and the license information.

```python
include pyproject.toml

# Include the README
include *.md

# Include the license file
include LICENSE.txt
```

### setup.py

The setup script "setup.py" defines the installation process.

It imports the required functions and classes from setup tools:
```python
from setuptools import setup, find_packages, Extension
```

It builds a list of the compiled extensions:
```python
extensions = []

# C extension called via ctypes
extensions.append(
        Extension(
            # "name" defines the location of the compiled module 
            # within the package tree:
            name='pypkgexample.mymodule_c_with_ctypes.hellofcctyp',
            # "sources" are the source files to be compiled
            sources=[('pypkgexample/mymodule_c_with_ctypes/'
                        + 'hellofunctions.c')]),
            # Here one can add compilation flags, libraries, 
            # macro declarations, etc. See setuptools documentation.
        )

# C extension called via cython
extensions.append(
        Extension(
            name='pypkgexample.mymodule_c_with_cython.hellofccyth', 
            sources=[('pypkgexample/mymodule_c_with_cython/'
                        + 'hellocython.pyx')],
            include_dirs=['./mymodule/mymodule_c_with_cython/']
        ))

# f2py extension 
# (to handle f2py extensions we need toreplace setup and 
# Extension with numpy ones)
from numpy.distutils.core import Extension
from numpy.distutils.core import setup
extensions.append(
        Extension(
            name='pypkgexample.mymodule_fortran.helloffort',
            sources=['pypkgexample/mymodule_fortran/hello_subr.f90'])
        )
```

```python

# If there are cython extension
from Cython.Build import cythonize
extensions = cythonize(extensions)

#########
# Setup #
#########

setup(
    name='pypkgexample',
    version='0.0.0',
    description='Example python package with compiled extensions',
    url='https://github.com/giadarol/pypkgexample',
    author='Giovanni Iadarola',
    packages=find_packages(),
    ext_modules = extensions,
    install_requires=[
        'numpy>=1.0',
        'pytest', # In principle could be made optional
        ]
    )
```


## References
The following resources were used in preparing this package.

### On python packaging

https://www.bernat.tech/pep-517-and-python-packaging/

https://packaging.python.org/guides/distributing-packages-using-setuptools/

https://packaging.python.org/tutorials/packaging-projects/

https://setuptools.readthedocs.io/en/latest/userguide/quickstart.html

https://github.com/pypa/sampleproject (sample project)

https://www.bernat.tech/pep-517-518/

https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/


### Packaging cython extensions

https://levelup.gitconnected.com/how-to-deploy-a-cython-package-to-pypi-8217a6581f09

https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#distributing-cython-modules

https://github.com/FedericoStra/cython-package-example (sample project)


### Packaging f2py extensions

https://numpy.org/devdocs/f2py/distutils.html

https://numpy.org/devdocs/f2py/f2py.getting-started.html


### Packaging C extensions using cython

https://docs.python.org/3.8/extending/building.html

https://pgi-jcns.fz-juelich.de/portal/pages/using-c-from-python.html


### Additional material

Comparison cython vs swig:

https://us.pycon.org/2013/schedule/presentation/111/

Comparison cffi cython pybind11:

http://blog.behnel.de/posts/cython-pybind11-cffi-which-tool-to-choose.html

https://iscinumpy.gitlab.io/post/tools-to-bind-to-python/

Comparison swig vs pybind11:

https://indico.cern.ch/event/974806/contributions/4104878/attachments/2158553/3641806/CMW-Python-Dec2020-Piotr.pdf


