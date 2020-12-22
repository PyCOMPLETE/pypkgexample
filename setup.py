from setuptools import setup, find_packages, Extension

extensions = []
# C extension to be used with ctypes
extensions.append(
        Extension(
            # "name" defines the location of the compiled module 
            # within the paccage tree:
            name = 'hellofrom.hellofrom_c_with_ctypes.hellofcctyp',
            # "sources" are the source files to be compiled
            sources = [('./hellofrom/hellofrom_c_with_ctypes/'
                        + 'hellofunctions.c')]),
            # Here one can add compilation flags, libraries, 
            # macro declarations, etc. See setuptools documentation.
        )


# f2py extension (to handle f2py extensions we need to 
# replace setup and Extension with numpy ones)
from numpy.distutils.core import Extension
from numpy.distutils.core import setup
extensions.append(
        Extension(
            name = 'hellofrom.hellofrom_fortran.helloffort',
            sources = ['./hellofrom/hellofrom_fortran/hello_subr.f90'])
            # Here one can add compilation flags, 
            # libraries, macro declarations, etc.
        )

# Setup
setup(
    name='hellofrom',
    packages=find_packages(),
    ext_modules = extensions,
    install_requires=[
        'numpy>=1.0',
        'pytest', # In principle could be made optional
        ]
    )
