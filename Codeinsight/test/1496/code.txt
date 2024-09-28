def test(dict0, var0, var1):
    return dict(filter(lambda item: var0 < item[0] < var1, dict0.items()))
