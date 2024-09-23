def test(var0, lst0):
    s = set()
    return [x for x in lst0 if x[var0] not in s and not s.add(x[var0])]
