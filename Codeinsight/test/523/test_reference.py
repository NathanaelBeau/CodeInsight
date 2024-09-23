def test(lst0, tpl0):
    result = [tuple([i + j for i, j in zip(e, tpl0)]) for e in lst0]
    return result
