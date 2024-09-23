import pandas as pd

def test(df1, df2, var0):
	return pd.concat([df1[var0], df2[var0]], axis=1, keys=['df1', 'df2'])
