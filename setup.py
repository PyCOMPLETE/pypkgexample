from setuptools import setup, find_packages

# f2py extension (to handle f2py extensions we need to 
# replace setup and Extension with numpy ones)
from numpy.distutils.core import Extension
from numpy.distutils.core import setup
ext1 = Extension(
        name = 'hellofrom.hellofrom_fortran.helloffort',
        sources = ['./hellofrom/hellofrom_fortran/hello_subr.f90'])

# Setup
setup(
    name='hellofrom',
    packages=find_packages(),
    ext_modules = [ext1],
    install_requires=[
        'numpy>=1.0',
        'pytest', # In principle could be made optional
        ]
    )
