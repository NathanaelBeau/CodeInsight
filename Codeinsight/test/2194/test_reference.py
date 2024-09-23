import numpy as np

def test(arr0, var0, var1):
    return len(np.where((arr0 >= var0) & (arr0 <= var1))[0])
