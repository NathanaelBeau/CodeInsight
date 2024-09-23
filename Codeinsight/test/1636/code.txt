import numpy as np
def test(arr0):
    try:
        return np.isnan(arr0.astype(float)).any()
    except ValueError:
        return True
