import numpy as np
def test(lst0, var0):
    arr = np.array(lst0)
    return [tuple(x) for x in np.argwhere(arr == var0)]
