def test(x, s):
    return max(loc for loc, val in enumerate(s) if val == x)