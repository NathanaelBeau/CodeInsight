import operator

def test(var0):
	return sorted(var0.items(), key=operator.itemgetter(1))



