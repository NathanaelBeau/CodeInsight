def test(str0, var0):
    return ' '.join(str0[i:i+var0] for i in range(0, len(str0), var0))
