def test(lst0, var0, var1):
    return [d for d in lst0 if d.get(var0) == var1] + [d for d in lst0 if d.get(var0) != var1]



