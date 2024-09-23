def test(df0, var0, var1):
	return  df0.loc[df0[var1] == 1, var0].sum()
