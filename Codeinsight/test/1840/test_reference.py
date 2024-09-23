def test(lst0, lst1):
	if lst0 == []:
		return []
	return list(list(zip(*sorted(zip(lst1,lst0))))[1]) 
