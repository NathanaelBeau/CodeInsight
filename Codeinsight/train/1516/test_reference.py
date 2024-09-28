def test(var0, dct0):
    if var0 in dct0:
        return dct0[var0]
    for k, v in dct0.items():
        if isinstance(v,dict):
            item = test(var0, v)
            if item is not None:
                return item
