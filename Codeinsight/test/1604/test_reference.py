def test(x, s):
    return len(s) - 1 - s[::-1].index(x)