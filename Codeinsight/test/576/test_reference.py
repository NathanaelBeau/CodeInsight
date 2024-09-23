def test(lst0, lst1):
    result = 0
    for i in range(len(lst0)):
        result += lst0[i] * lst1[i]
    return result
