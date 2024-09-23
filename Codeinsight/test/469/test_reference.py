import numpy as np

def test(var0, var1):
	diff = np.setdiff1d(var1, var0)
	if diff.size:
		return False
	else:
		return True
