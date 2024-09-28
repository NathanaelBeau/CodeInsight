def test(lst0):
    result = []
    [result.append(i) for i in lst0 if i not in result]
    return result