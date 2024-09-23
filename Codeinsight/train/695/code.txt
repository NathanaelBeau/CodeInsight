import numpy as np

def test(arr0, var0):
    rounded_arr = np.round(arr0, var0)
    return rounded_arr.astype(str)