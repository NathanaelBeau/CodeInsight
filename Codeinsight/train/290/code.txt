import numpy as np

def test(arr0, var0, var1):
    return arr0[np.ix_(var0, var1)]
