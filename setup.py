from setuptools import setup, find_packages

from numpy.distutils.core import Extension as npExtension
from numpy.distutils.core import setup

ext1 = npExtension(
        name = 'hffortran',
        sources = ['./hellofrom/hello_from_fortran/sqrt_array.f90'])

setup(
    name='hellofrom',
    packages=find_packages(),
    ext_modules = [ext1],
    install_requires=[
        'numpy>=1.0',
        'pytest', # This could be made optional but we don't do it 
        ]
    )
