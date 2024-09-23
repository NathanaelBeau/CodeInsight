import numpy as np

def test(arr0, var0, var1):
    return np.array(list(arr0), np.uint8).reshape(var0, var1, 4)

