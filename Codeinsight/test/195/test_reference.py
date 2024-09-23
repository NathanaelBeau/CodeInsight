def test(lst0, var0, var1):
    stripped_result = [s.strip(var0) for s in lst0]
    replaced_result = [s.replace(var0, var1) for s in lst0]
    return replaced_result
