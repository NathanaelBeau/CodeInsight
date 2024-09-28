def test(lst0):
	def try_int(x):
		try:
			return int(x)
		except ValueError:
			return x
	return [try_int(x) for x in lst0]