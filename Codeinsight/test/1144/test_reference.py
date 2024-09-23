def test(dict0, var0, var1):
    return {k: v for k, v in dict0.items() if var0 < k < var1}
