def test(str0):
    t = iter(str0)
    return '-'.join(a + b for a, b in zip(t, t))
