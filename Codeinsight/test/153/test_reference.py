import numpy as np
def test(lst0):
    array0 = np.array(lst0, dtype=object)
    return np.concatenate(array0).ravel()
