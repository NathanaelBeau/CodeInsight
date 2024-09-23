import numpy as np

def test(var0, var1):
	return list(np.linspace(var0, var1, var1 - var0, endpoint=False))
