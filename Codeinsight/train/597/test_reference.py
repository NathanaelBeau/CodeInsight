def test(lst0, var0, lst1):
    result = []
    for x in lst0:
        if x[var0] not in lst1:
            result.append(x)
    return result
