def test(var0, var1):
    result = [sum(var0[i] * col[i] for i in range(len(var0))) for col in zip(*var1)]
    return result
