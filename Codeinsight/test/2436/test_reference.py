def test(lst0, lst1):
    result = 0
    for x, y in zip(lst0, lst1):
        result += x * y
    return result

