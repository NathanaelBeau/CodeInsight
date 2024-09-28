import numpy as np
def test(matrix0, var0):
    return np.hsplit(matrix0, [var0])[0]
