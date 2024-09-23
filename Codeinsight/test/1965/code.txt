import numpy as np
def test(arr0):
    if arr0.size == 0:
        return []
    return [item for item in np.nditer(arr0)]