def test(lst0, var0, var1):
    return any(d.get(var0) == var1 for d in lst0)

