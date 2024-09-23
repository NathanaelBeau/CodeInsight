def test(var0):
    if len(var0) < 1:
        return []
    else:
        return [int(s) for s in var0.split(',')]
