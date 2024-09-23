def test(var0, lst0):
    return any(var0.startswith(prefix) for prefix in lst0)