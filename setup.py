from setuptools import setup, find_packages, Extension

#######################################
# Prepare list of compiled extensions #
#######################################

extensions = []

# C extension called via ctypes
extensions.append(
        Extension(
            # "name" defines the location of the compiled module 
            # within the paccage tree:
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
# Cython extensions need to be cythonized before being added to main
# extension list:
extensions += cythonize(cython_extensions)



# f2py extension 
# (to handle f2py extensions we need to replace the setup function and 
# the Extension class with their exteded version from numpy ones)
from numpy.distutils.core import Extension
from numpy.distutils.core import setup
extensions.append(
        Extension(
            name='pypkgexample.mymodule_fortran.helloffort',
            sources=['pypkgexample/mymodule_fortran/hello_subr.f90'])
        )

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
