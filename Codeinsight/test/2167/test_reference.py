import numpy as np

def test(arr0, var0, var1, var2):
    sliced_array = arr0[var0, var1]
    extended_array = np.vstack([sliced_array, np.tile(sliced_array[-1, :], (var2, 1))])
    return extended_array
