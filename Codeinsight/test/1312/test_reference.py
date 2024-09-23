from operator import itemgetter

def test(lst0, var0):
	return [*map(itemgetter(var0), lst0)]
