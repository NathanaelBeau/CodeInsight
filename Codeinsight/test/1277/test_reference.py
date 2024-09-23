import numpy as np
def test(arr0, var0):
    arr0 = np.array(arr0)
    arr0 = arr0[arr0 < var0]
    return arr0.tolist()
    
