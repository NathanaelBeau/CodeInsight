def test(lst0):
    result = []
    for x in lst0:
        result.append((x,))
    return tuple(result)