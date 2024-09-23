import numpy as np
def test(lst0, lst1):
    return np.mean((lst0 - lst1)**2)
