import pandas as pd

def test(var0, var1, var2):
	var0.sort_values(by=[var1], key=lambda x: x.map(var2), inplace=True)
	return var0.reset_index(drop=True)
