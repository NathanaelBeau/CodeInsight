import pandas as pd

def test(var0):
	df_values = var0.values
	df_values.sort(axis=1)
	df_values_sorted = df_values[:, ::-1]
	return pd.DataFrame(df_values_sorted, var0.index, var0.columns)