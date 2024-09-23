from itertools import chain

def test(lst0, lst1):
	return list(chain(*zip(lst0,lst1)))

