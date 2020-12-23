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
            name='hellofrom.hellofrom_c_with_ctypes.hellofcctyp',
            # "sources" are the source files to be compiled
            sources=[('./hellofrom/hellofrom_c_with_ctypes/'
                        + 'hellofunctions.c')]),
            # Here one can add compilation flags, libraries, 
            # macro declarations, etc. See setuptools documentation.
        )

# C extension called via cython
extensions.append(
        Extension(
            name='hellofrom.hellofrom_c_with_cython.hellofccyth', 
            sources=[('./hellofrom/hellofrom_c_with_cython/'
                        + 'hellocython.pyx')],
            include_dirs=['./hellofrom/hellofrom_c_with_cython/']
        ))

# f2py extension 
# (to handle f2py extensions we need toreplace setup and 
# Extension with numpy ones)
from numpy.distutils.core import Extension
from numpy.distutils.core import setup
extensions.append(
        Extension(
            name='hellofrom.hellofrom_fortran.helloffort',
            sources=['./hellofrom/hellofrom_fortran/hello_subr.f90'])
        )


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
