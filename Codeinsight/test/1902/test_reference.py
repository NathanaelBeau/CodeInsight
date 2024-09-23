import numpy as np
def test(arr0, dict0, default_value=np.nan):
    vfunc = np.vectorize(lambda x: dict0.get(x, default_value))
    return vfunc(arr0)