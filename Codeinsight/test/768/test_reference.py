import numpy as np

def test(arr0, arr1):
    subs = arr0 - arr1
    out = np.sqrt(np.einsum('i,i->', subs, subs))
    return out

