import numpy as np

def test(var0, var1, var2):
    sliced = np.hstack(var0[:, var1:var2])
    return sliced

