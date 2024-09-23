def test(lst0, lst1):
    result = []
    for x, y in zip(lst0, lst1):
        result.append(x == y)
    return result

