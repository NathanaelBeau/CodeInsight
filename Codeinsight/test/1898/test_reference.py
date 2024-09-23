import numpy as np
def test(arr0, lst0, lst1):
    return arr0[np.ix_(lst0, lst1)]


