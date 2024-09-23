import numpy as np
def test(matrix0, var0):
    return np.take(matrix0, range(var0), axis=1)

