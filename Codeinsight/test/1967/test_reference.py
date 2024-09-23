def test(var0, var1):
    result = [sum(v * c for v, c in zip(var0, col)) for col in zip(*var1)]
    return result
