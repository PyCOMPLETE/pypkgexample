import numpy as np

import hellofrom as hf

a = np.array([9., 4., 1.])

print(f'From python: {hf.sqrt_array_python(a)}')
print(f'From Fortran via f2py: {hf.sqrt_array_fortran(a)}')
print(f'From C via ctypes: {hf.sqrt_array_c_ctypes(a)}')
print(f'From C via cython: {hf.sqrt_array_c_cython(a)}')
