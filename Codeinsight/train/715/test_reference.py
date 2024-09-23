def test(var0, var1, var2):
    parts = var0.split(var1, var2)
    if len(parts) <= var2:
        return -1
    return len(var0) - len(parts[-1]) - len(var1)
