import numpy as np

def test(lst0):
    la = len(lst0)
    arr = np.array(np.meshgrid(*lst0)).T.reshape(-1, la)
    arr = [tuple(map(str, row)) for row in arr]
    return arr
