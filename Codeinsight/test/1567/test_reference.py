import numpy as np

def test(var0, var1):
	return np.isin(var1, var0).all()