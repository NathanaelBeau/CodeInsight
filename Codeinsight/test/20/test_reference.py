def test(var0):
	return [dict(s) for s in set(frozenset(d.items()) for d in var0)]
