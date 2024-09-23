def test(lst0, var0):
    return sorted(lst0, key=lambda x: getattr(x, var0), reverse=True)
