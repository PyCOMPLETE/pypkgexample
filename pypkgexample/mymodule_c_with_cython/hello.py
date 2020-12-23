import numpy as np
from . import hellofccyth as _hc

def sqrt_array(vect):
    npvect = np.float_(vect)
    res = np.empty_like(npvect)
    _hc.sqrt_array(npvect, res)
    return res

def say_hello():
    _hc.say_hello()
