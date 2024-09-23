import numpy as np
def test(lst0):
    unique, inverse = np.unique(lst0, return_inverse=True)
    rank = np.empty_like(inverse)
    np.put(rank, np.argsort(inverse, kind='mergesort'), np.arange(len(lst0)))
    return rank