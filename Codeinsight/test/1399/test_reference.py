import numpy as np
from numpy import array
def test(var0) :
    return np.isnan(var0).sum() / np.prod(var0.shape)
