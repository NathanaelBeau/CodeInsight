import numpy as np

def test(lst0, lst1):
    average = np.average(lst0, weights=lst1)
    return np.sqrt(np.average((lst0-average)**2, weights=lst1))

