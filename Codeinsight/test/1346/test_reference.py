import numpy as np

def test(lst0, lst1):
    return np.linalg.norm(np.array(lst0) - np.array(lst1))
