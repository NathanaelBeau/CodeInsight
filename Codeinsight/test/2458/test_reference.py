def test(str0):
    return sorted(str0, key=lambda x: (x.isupper(), x))
