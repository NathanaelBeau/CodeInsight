import numpy as np

def test(arr0, var0):
    formatted_arr = np.array([var0.format(x) for x in arr0])
    return formatted_arr.tolist()
