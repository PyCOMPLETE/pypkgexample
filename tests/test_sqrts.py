import hellofrom as hf
import numpy as np

def test_sqrt_python():
    assert np.max(
            hf.sqrt_array_python([1., 4., 9.])-
          -  np.array([1., 2., 3.])) < 1e30

def test_sqrt_fortran():
    assert np.max(
            hf.sqrt_array_fortran([1., 4., 9.])-
          -  np.array([1., 2., 3.])) < 1e30

def test_sqrt_c_ctypes():
    assert np.max(
            hf.sqrt_array_c_ctypes([1., 4., 9.])-
          -  np.array([1., 2., 3.])) < 1e30
