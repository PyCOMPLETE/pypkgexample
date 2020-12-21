import hellofrom as hf
import numpy as np

def test_sqrt_python():
    assert np.max(
            hf.sqrt_array_python([1., 4., 9.])-
          -  np.array([1., 2., 3.])) < 1e30
