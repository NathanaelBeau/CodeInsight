import numpy as np

def test(arr0):
    return np.unravel_index(arr0.argmax(), arr0.shape)

