import numpy as np
def test(lst0, var0):
    lst0 = np.asarray(lst0)
    distances = np.abs(lst0 - var0)
    nearest_index = np.argpartition(distances, 0)[0]
    return lst0[nearest_index]
