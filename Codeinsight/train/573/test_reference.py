def test(lst0):
    result_dict = {}
    for x, y in lst0:
        result_dict.setdefault(x, []).append(y)
    return result_dict
