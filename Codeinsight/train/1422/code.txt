def test(lst0, tpl0):
    result = []
    for tup in lst0:
        new_tup = tuple(i + j for i, j in zip(tup, tpl0))
        result.append(new_tup)
    return result
