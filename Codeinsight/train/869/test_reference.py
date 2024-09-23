import numpy as np

def test(shape0, var0):
    if var0:
        return np.ones(shape0, dtype=bool)
    else:
        return np.zeros(shape0, dtype=bool)

