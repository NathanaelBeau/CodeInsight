import pandas as pd

def test(var0, var1, var2):
	var1[var0] = var1[var0].fillna(var1[var2])
	return var1