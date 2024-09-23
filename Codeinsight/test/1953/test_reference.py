import numpy as np
import itertools
def test(arr0):
    values = np.array(list(zip(*[(key, len(list(group))) for key, group in itertools.groupby(arr0)])))
    return values

