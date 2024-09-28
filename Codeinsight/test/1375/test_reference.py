def test(str0):
    return '-'.join(a + b for a, b in zip(str0[::2], str0[1::2]))

