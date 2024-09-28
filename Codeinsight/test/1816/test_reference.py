import numpy as np

def test(a, var0, var1):
    return np.sum((a > var0) & (a <= var1))