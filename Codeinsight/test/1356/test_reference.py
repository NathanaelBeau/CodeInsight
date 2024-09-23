import numpy as np

def test(value):
    return isinstance(value, (np.generic, np.ndarray))

