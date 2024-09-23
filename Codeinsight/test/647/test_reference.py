import numpy as np
def test(arr0, var0, var1):
    new_shape = (arr0.shape[0] + var0, arr0.shape[1] + var1)
    expanded_arr = np.zeros(new_shape)
    expanded_arr[:arr0.shape[0], :arr0.shape[1]] = arr0
    return expanded_arr

