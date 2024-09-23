def test(dict0, var0):
    return dict(sorted(dict0.items(), key=lambda x: x[1][var0]))
