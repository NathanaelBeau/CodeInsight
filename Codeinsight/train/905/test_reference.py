import numpy as np

def test(arr0, var1):
    return arr0[np.arange(arr0.shape[0])!= var1,:,:]
