import numpy as np

def test(lst0):
    inverted_array = ~np.array(lst0)
    return list(inverted_array)
