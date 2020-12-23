from ._version import __version__

from .mymodule_python.hello import say_hello as say_hello_python
from .mymodule_python.hello import sqrt_array as sqrt_array_python

from .mymodule_fortran.hello import sqrt_array as sqrt_array_fortran
from .mymodule_fortran.hello import say_hello as say_hello_fortran

from .mymodule_c_with_ctypes.hello import sqrt_array as sqrt_array_c_ctypes
from .mymodule_c_with_ctypes.hello import say_hello as say_hello_c_ctypes


from .mymodule_c_with_cython.hello import sqrt_array as sqrt_array_c_cython
from .mymodule_c_with_cython.hello import say_hello as say_hello_c_cython
