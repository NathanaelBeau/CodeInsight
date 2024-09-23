def test(lst0, var0):
    stripped_result = [s.strip(var0) for s in lst0]
    replaced_result = [s.replace(var0, '') for s in lst0]
    return  replaced_result
