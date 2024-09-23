import operator

def test(lst0):
	lst0.sort(key=operator.itemgetter(1))
	return lst0