def test(lst0, var0):
	return len(lst0) - 1 - lst0[::-1].index(var0)
