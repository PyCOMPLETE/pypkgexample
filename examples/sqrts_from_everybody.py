import numpy as np

import pypkgexample as pe

a = np.array([9., 4., 1.])

print(f'From python: {pe.sqrt_array_python(a)}')
print(f'From Fortran via f2py: {pe.sqrt_array_fortran(a)}')
print(f'From C via ctypes: {pe.sqrt_array_c_ctypes(a)}')
print(f'From C via cython: {pe.sqrt_array_c_cython(a)}')
