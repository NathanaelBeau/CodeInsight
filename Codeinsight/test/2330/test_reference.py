def test(dict0, var0, var1):
    return dict((k, v) for k, v in dict0.items() if var0 < k < var1)
