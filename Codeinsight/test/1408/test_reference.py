import numpy as np
def test(arr0):
    non_nan_elements = filter(lambda x: not np.isnan(x), arr0)
    return len(list(non_nan_elements))

