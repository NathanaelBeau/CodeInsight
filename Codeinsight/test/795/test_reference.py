import numpy as np
def test(arr0):
    count = sum(1 for element in arr0 if not np.isnan(element))
    return count

