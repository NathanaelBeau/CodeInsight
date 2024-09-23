def test(var1, var2):
	n = var1**var2
	ans = sum(int(c) for c in str(n))
	return ans
