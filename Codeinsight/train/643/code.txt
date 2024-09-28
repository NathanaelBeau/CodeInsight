import numpy as np

def test(arr0, var0):
    return np.hstack((arr0[:,:var0], arr0[:,var0+1:]))
