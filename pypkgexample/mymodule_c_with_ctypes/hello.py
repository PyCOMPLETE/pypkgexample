from pathlib import Path
import sysconfig
import ctypes

import numpy as np

# We need a bit of gymnastics to retrive the shared 
# library path
thisfolder = Path(__file__).parent.absolute()
suffix = sysconfig.get_config_var('EXT_SUFFIX')

# Load compiled shared library
_hc = ctypes.CDLL(thisfolder.joinpath(
    'hellofcctyp' + suffix))

# Define interface to be usable with numpy array
nd_pointer = np.ctypeslib.ndpointer(
        dtype=np.float64, ndim=1, flags="C")
_hc.sqrt_array.argtypes = (nd_pointer, ctypes.c_int, nd_pointer)

# Python wrapping function
def sqrt_array(vect):
    vect_arr = np.float_(vect)
    res = np.empty_like(vect_arr)
    _hc.sqrt_array(vect_arr, len(vect_arr), res)
    return(res)

def say_hello():
    _hc.say_hello()
