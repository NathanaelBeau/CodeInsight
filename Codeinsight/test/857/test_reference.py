import numpy as np
from scipy.spatial.distance import cdist 
def test(lst0, lst1, var0, var1):
    distances = cdist([(var0, var1)], np.vstack((lst0, lst1)).T)
    return np.argmin(distances)


