def test(lst0, lst1):
    result = []
    for a, b in zip(lst0, lst1):
        result.extend([a, b])
    result.extend(lst0[len(lst1):] or lst1[len(lst0):])
    return result
