import numpy as np

def test(lst0):
    _, numbers = np.unique(lst0, return_inverse=True)
    return numbers


