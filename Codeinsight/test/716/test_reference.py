import numpy as np
def test(arr0):
    sorted_unique_values, index = np.unique(arr0, return_index=True)
    return sorted_unique_values[np.argsort(index)]
