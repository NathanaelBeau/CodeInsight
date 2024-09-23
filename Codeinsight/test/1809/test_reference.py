def test(lst0):
	dictionary = {}
	for sublist in lst0:
		if len(sublist) == 2:
			key, value = sublist
			dictionary[key] = value
		else:
			pass
	return dictionary
