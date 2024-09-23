import pandas as pd

def test(var0, var1, var2):
	mydf = var2.groupby([var0,var1]).size().reset_index()
	mydf.rename(columns = {0: 'frequency'}, inplace = True)
	return mydf