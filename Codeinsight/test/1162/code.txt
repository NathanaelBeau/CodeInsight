def test(lst0, tpl0):
    result = [(i + tpl0[0], j + tpl0[1], k + tpl0[2]) for i, j, k in lst0]
    return result
