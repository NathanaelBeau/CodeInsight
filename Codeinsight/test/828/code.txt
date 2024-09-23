import numpy as np
def test(lst0, lst1):
    diff = np.subtract(lst0, lst1)
    squared_diff = np.power(diff, 2)
    return np.mean(squared_diff)
