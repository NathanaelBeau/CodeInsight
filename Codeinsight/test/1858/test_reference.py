import numpy as np
def test(lst0, var0):
    return list(np.where(np.array(lst0) == var0)[0])

