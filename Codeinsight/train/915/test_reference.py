def test(df0, var0, var1):
	try:
		return df0.groupby(var1)[var0].sum()[1]
	except:
		return 0