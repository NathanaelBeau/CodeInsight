def test(lst0, var0):
	return next(i for i in reversed(range(len(lst0))) if lst0[i] == var0)
