def test(dict0, var0):
    return {k: var0 for k, v in dict0.items() if v is None}
