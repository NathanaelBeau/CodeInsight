def test(var0, var1):
    split_index = var0.rfind(var1)
    if split_index == -1:
        return var0
    else:
        return var0[:split_index]
