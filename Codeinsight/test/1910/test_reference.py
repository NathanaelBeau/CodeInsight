def test(lst0, var0):
    result = {}
    for d in lst0:
        key = d.pop(var0)
        result[key] = d
    return result

