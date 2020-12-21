from setuptools import setup, find_packages

setup(
    name='hellofrom',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.0',
        'pytest', # This could be made optional but we don't do it 
        ]
    )
