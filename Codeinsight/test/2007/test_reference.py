def test(var0, dict0):
    return len(list(filter(lambda x:x.get(var0, False), dict0)))