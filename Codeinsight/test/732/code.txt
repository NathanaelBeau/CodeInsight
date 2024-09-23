def test(str0, str1):
    return sum(1 for w in str0.lower().split() if w == str1.lower())
	