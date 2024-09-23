def test(lst0, var0):
    result = []
    for x in lst0:
        if not var0(x):
            result.append(x)
    return result

