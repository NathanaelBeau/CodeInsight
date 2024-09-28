import numpy as np
def test(lst0, var0):
    return list(np.array(lst0)[np.array(lst0) > var0])