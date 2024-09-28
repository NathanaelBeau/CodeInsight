def test(str0):
    return '-'.join(str0[i:i+2] for i in range(0, len(str0), 2))
