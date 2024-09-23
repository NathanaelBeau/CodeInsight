import numpy as np
def test(lst0, lst1, var0, var1):
    distances = np.sqrt((lst0-var0)**2 + (lst1-var1)**2)
    return np.argmin(distances)


