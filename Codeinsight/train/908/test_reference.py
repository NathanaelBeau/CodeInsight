def test(var0):
    if len(var0) < 1:
        return []
    else:
        return list(map(int, var0.split(',')))
