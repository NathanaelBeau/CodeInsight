import numpy as np
def test(arr0):
    return arr0.view(np.float64).reshape(arr0.shape + (-1,))
