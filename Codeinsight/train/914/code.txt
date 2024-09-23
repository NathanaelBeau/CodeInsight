def test(lst0, var0, var1):
	return all(var0 == var1 for (_, _, var0) in lst0)