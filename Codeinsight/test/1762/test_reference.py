import re

def test(var0):
	res = re.split('([.?!])', var0)
	res = [value for value in res if value.strip()]
	return [''.join(res[i:i+2]) for i in range(0, len(res), 2)]