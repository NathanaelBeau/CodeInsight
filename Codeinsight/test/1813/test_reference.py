def test(dict0, var0, var1, var2):
    return {k: dict0.get(k, None) for k in (var0, var1, var2)}

