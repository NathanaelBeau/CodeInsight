def test(str0, var0):
    return var0.join(a + b for a, b in zip(str0[::2], str0[1::2]))


