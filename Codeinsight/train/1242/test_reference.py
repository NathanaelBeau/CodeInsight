def test(str0):
    x = list(str0)
    x.remove("'")
    return ''.join(x)