def test(var0, var1):
	return next((i for i, v in enumerate(var0) if v[0] == var1), None)
