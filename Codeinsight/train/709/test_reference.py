import numpy as np

def test(arr0, var0, var1):
    return np.sum((arr0 >= var0) & (arr0 <= var1))

