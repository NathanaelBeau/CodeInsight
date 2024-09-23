import numpy as np
def test(arr0):
    non_zero_values = arr0[arr0 != 0]
    return non_zero_values.min(), non_zero_values.max()

