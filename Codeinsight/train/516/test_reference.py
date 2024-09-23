def test(dict0, var0):
    for key, val in dict(dict0).items():
        if val == var0:
            del dict0[key]
    return dict0
