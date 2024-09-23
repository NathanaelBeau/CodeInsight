def test(var0, var1):
	sorted_dict = {}
	for s in sorted(var0.items(), key=lambda k_v: k_v[1][var1]):
		sorted_dict[s[0]] = s[1]
	return sorted_dict