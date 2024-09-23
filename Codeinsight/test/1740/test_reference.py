import numpy as np
def test(arr0, dict0, default_value=np.nan):
    return np.array([dict0.get(item, default_value) for item in arr0])