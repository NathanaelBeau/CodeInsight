def test(lst0, lst1):
	return [j for i in zip(lst0,lst1) for j in i]
