import numpy as np
def test(arr0):
    min_value = np.min(arr0[arr0 != 0])
    max_value = np.max(arr0[arr0 != 0])
    return min_value, max_value

