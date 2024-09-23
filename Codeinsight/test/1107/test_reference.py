def test(lst0, var0):
    return [{k: v for k, v in d.items() if k != var0} for d in lst0]
