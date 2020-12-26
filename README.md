# pypkgexample

## Table of contents
 - [Introduction](#introduction) 
 - [Tasks performed by pypkgexample](#tasks-performed-by-pypkgexample)
 - [Structure of the package](#structure-of-the-package)
 - [Installation code](#installation-code)
 - [Python bindings to C and Fortran](#python-bindings-to-c-and-fortran)
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

```pypkgexample``` performs two tasks for illustration purposes:
 - it says "hello";
 - it computes the square root of an array (to illustrate how to pass a python array to Fortran or C compiled code).
 
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

```pypkgexample``` has the structure used for standard python packages. It consists in a folder named after the package "pypkgexample" (which is also the top level of the git repository) that contains the source code, the required code and information for the installation, documentation, unit tests and usage examples. In particular:
 - The **source code** is contained in a subfolder that also has the same name of the python package (pypkgexample).
 - **Unit tests** is contained in the folder "tests" and can be executed using [pytest](http://pytest.org)
 - **Examples** illustrating the package usage are hosted in the folder "examples"
 - **License** information is contained in the file "LICENSE.txt"
 - This **documentation** is contained in the file "README.md"
 - The **installation process** is defined by the files ["pyprocjet.toml"](#pyprojecttoml), ["MANIFEST.in"](#manifestin), and  ["setup.py"](#setuppy), which will be described in more detail in the following section.
 
## Installation code

The build and installation process is performed by the pip pacakge installer based on the following files:

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

The file "MANIFEST.in" defines the additional files that need to be copied together with the installed package, together with those that are strictly required for the package to work. In our case we include, "pyproject.toml", this readme file and the license information.

```python
include pyproject.toml

# Include the README
include *.md

# Include the license file
include LICENSE.txt
```

### setup.py

The setup script "setup.py" defines the installation process, by performing the following steps

The required functions and classes are imported from the setuptools library:
```python
from setuptools import setup, find_packages, Extension
```

A list of the extensions to be compiled is built. In our case this includes a C extension to be used with ctypes bindings, a C extension with cython bindings and a Fortran extension with f2py bindings. For each extension its location within the package tree is specified, together with the list of the source files (C, Fortran and cython files) to be compiled. Libraries to be linked, header files to be included, compilation flags can be specified as additional keywords (for details, see setuptools documentation).
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
                        + '/src/hellofunctions.c')],
            include_dirs=[('pypkgexample/mymodule_c_with_ctypes'
                        + '/include')],
            # Here one can add compilation flags, libraries, 
            # macro declarations, etc. See setuptools documentation.
            )
        )

# C extension called via cython
from Cython.Build import cythonize
cython_extensions = [
        Extension(
            name='pypkgexample.mymodule_c_with_cython.hellofccyth', 
            sources=[('pypkgexample/mymodule_c_with_cython/'
                        + 'hellocython.pyx'),
                     ('pypkgexample/mymodule_c_with_cython/'
                        + '/src/hellofunctions.c')],
            include_dirs=[('pypkgexample/mymodule_c_with_cython'
                        + '/include')],
        ),
        # Other cython extensions can be added here
    ]
# Cython extensions need to be cythonized before being added to the main
# extension list:
extensions += cythonize(cython_extensions)


# f2py extension 
# (to handle f2py extensions we need to replace the setup function and 
# the Extension class with their extended version from the numpy package)
from numpy.distutils.core import Extension
from numpy.distutils.core import setup
extensions.append(
        Extension(
            name='pypkgexample.mymodule_fortran.helloffort',
            sources=['pypkgexample/mymodule_fortran/hello_subr.f90'])
        )
```

The setup function is the one that actually builds the extensions and installs the package. Note that the package dependencies are specified by the "install_requires" argument. The pip package installer will automatically install the dependencies before the package installation.
```python
setup(
    name='pypkgexample',
    version='0.0.0',
    description='Example python package with compiled extensions',
    url='https://github.com/giadarol/pypkgexample',
    author='Giovanni Iadarola',
    packages=find_packages(), # finds all the packages in the folder
    ext_modules = extensions,
    install_requires=[
        'numpy>=1.0',
        'pytest', # In principle could be made optional
        ]
    )
```

## Python bindings to C and Fortran

In this section we will briefly discuss the examples of python bindings contained in the pypkgexample.

Note that the interface of the package is defined by the file ```__init__.py```, so that the different implementations of the functions "say_hello" and "sqrt_array" can be used as discussed [above](#tasks-performed-by-pypkgexample):
```python
from ._version import __version__

from .mymodule_python.hello import say_hello as say_hello_python
from .mymodule_python.hello import sqrt_array as sqrt_array_python

from .mymodule_fortran.hello import sqrt_array as sqrt_array_fortran
from .mymodule_fortran.hello import say_hello as say_hello_fortran

from .mymodule_c_with_ctypes.hello import sqrt_array as sqrt_array_c_ctypes
from .mymodule_c_with_ctypes.hello import say_hello as say_hello_c_ctypes

from .mymodule_c_with_cython.hello import sqrt_array as sqrt_array_c_cython
from .mymodule_c_with_cython.hello import say_hello as say_hello_c_cython
```

### Bindings to Fortran with f2py

The functions to be exposed to python are contained in a Fortran source file:
```fortran
! pypkgexample/pypkgexample/mymodule_fortran/hello_subr.f90

      subroutine sqrt_array(vect, vect_len, res)
      
        implicit none
        
        integer, intent(in)     :: vect_len
        real(kind=8), intent(in)        :: vect(vect_len)
        real(kind=8), intent(out)       :: res(vect_len)
        
        integer ::  i

        do i=1,vect_len
            res(i) = sqrt(vect(i))
        enddo 

      end subroutine
      

      subroutine say_hello()

        write(*,*), "Hello from Fortran!"

      end subroutine
```
f2py uses the intent annotations to define the interface of the corresponding python functions. Different options for achieving this are described in the f2py documentation.

The fortran source file gets compiled when executing [setup.py](#setuppy) (or pip install), based on our extension definition, producing a file called "pypkgexample/mymodule_fortran/helloffort.cpython-38-x86_64-linux-gnu.so", which can be imported in python by the statement:
```python
import pypkgexample.mymodule_fortran.helloffort
```
or, in python file in the mymodule_fortran module, simply as:
```python
from . import helloffort
```
as done for example in "pypkgexample/mymodule_fortran/hello.py".

### Bindings to C with cython
The C functions to be bound are defined by C header and a C source file:

```C
/* pypkgexample/pypkgexample/mymodule_c_with_cython/include/hellofunctions.h */

#ifndef HELLOFUNCTIONS_H
#define HELLOFUNCTIONS_H

#include <math.h>
#include <stdio.h>

void sqrt_array_c(double* vect, int vect_len, double* res); 
void say_hello_c();

#endif
```

```C
/* pypkgexample/pypkgexample/mymodule_c_with_cython/src/hellofunctions.c */

#include <hellofunctions.h>

void sqrt_array_c(double* vect, int vect_len, double* res) {
    int ii;
    for (ii = 0; ii < vect_len; ii++) {
       res[ii] = sqrt(vect[ii]); 
    }
}

void say_hello_c() {
    printf("Hello from C with cython!\n");
    fflush(stdout);
}
```

The interface to python is defined by a cython source file, form which the C functions can be directly called:
```cython
# pypkgexample/pypkgexample/mymodule_c_with_cython/hellocython.pyx

cdef extern from "hellofunctions.h" :
    void sqrt_array_c(double* vect, int vect_len, double* res)
    void say_hello_c()

def sqrt_array(double[::1] vect, double[::1] res):
    sqrt_array_c(&vect[0], len(vect), &res[0])

def say_hello():
    say_hello_c()
```
The module gets compiled when executing [setup.py](#setuppy) (or pip install), following our extension definition, producing a file called "pypkgexample/mymodule_c_with_cython/hellofccyth.cpython-38-x86_64-linux-gnu.so", which can be imported in python by the statement:
```python
import pypkgexample.mymodule_fortran.helloccyth
```
or by a python file in the mymodule_c_with_cython module simply as:
```python
from . import helloccyth
```
as done for example in "pypkgexample/mymodule_c_with_cython/hello.py".

### Bindings to C with ctypes
In this case the C functions to be bound are defined by C header and a C source file:

```C
/* pypkgexample/pypkgexample/mymodule_c_with_ctypes/include/hellofunctions.h */

#ifndef HELLOFUNCTIONS_H
#define HELLOFUNCTIONS_H

#include <math.h>
#include <stdio.h>

void sqrt_array_c(double* vect, int vect_len, double* res); 
void say_hello_c();

#endif
```

```C
/* pypkgexample/pypkgexample/mymodule_c_with_ctypes/src/hellofunctions.c */

#include <hellofunctions.h>

void sqrt_array_c(double* vect, int vect_len, double* res) {
    int ii;
    for (ii = 0; ii < vect_len; ii++) {
       res[ii] = sqrt(vect[ii]); 
    }
}

void say_hello_c() {
    printf("Hello from C with ctypes!\n");
    fflush(stdout);
}
```
The source gets compiled when executing [setup.py](#setuppy) (or pip install), based on our extension definition, producing a shared library file called "pypkgexample/mymodule_c_with_ctypes/hellofcctyp.cpython-38-x86_64-linux-gnu.so". This shared library cannot be imported in python with a simple import statement because it does not exposes the required interface. In can instead be imported in python using the "ctypes.CDLL" function.
This is done in the file pypkgexample/pypkgexample/mymodule_c_with_ctypes/hello.py. 

To do so,  the exact path of the shared object needs to be retrieved. This is done my identifying the path of the containing folder and by using the sysconfig builtin library to retrieve the suffix ".cpython-38-x86_64-linux-gnu.so" (which depends on the python version and operative system):

```python
from pathlib import Path
import sysconfig
import ctypes

import numpy as np

# We need a bit of gymnastics to retrive the shared 
# library path
thisfolder = Path(__file__).parent.absolute()
suffix = sysconfig.get_config_var('EXT_SUFFIX')

# Load compiled shared library
_hc = ctypes.CDLL(thisfolder.joinpath('hellofcctyp' + suffix))
```

For the C functions to be callable from C, their interface needs to be explicitly defined by:
```python
nd_pointer = np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C")
_hc.sqrt_array_c.argtypes = (nd_pointer, ctypes.c_int, nd_pointer)
```

The C function can then by called from python as done in the "hello.py" file:
```python
def sqrt_array(vect):
    vect_arr = np.float_(vect)
    res = np.empty_like(vect_arr)
    _hc.sqrt_array_c(vect_arr, len(vect_arr), res)
    return(res)
```



## References
The following resources were used for preparing this package and documentation.

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

### Structure of C project

https://hiltmon.com/blog/2013/07/03/a-simple-c-plus-plus-project-structure/

### Additional material

Comparison cython vs swig:

https://us.pycon.org/2013/schedule/presentation/111/

Comparison cffi vs cython vs pybind11:

http://blog.behnel.de/posts/cython-pybind11-cffi-which-tool-to-choose.html

https://iscinumpy.gitlab.io/post/tools-to-bind-to-python/

Comparison swig vs pybind11:

https://indico.cern.ch/event/974806/contributions/4104878/attachments/2158553/3641806/CMW-Python-Dec2020-Piotr.pdf


