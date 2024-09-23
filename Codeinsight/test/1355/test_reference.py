import numpy as np
import re

def test(df0, var0, lst0):
    pattern = '|'.join(lst0)
    vfunc = np.vectorize(lambda x: bool(re.search(pattern, x, re.I) if isinstance(x, str) else False))
    return df0[vfunc(df0[var0])]

