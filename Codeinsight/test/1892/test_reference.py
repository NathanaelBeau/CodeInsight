def test(lst0):
    seen = {}
    new_lst = [x for x in lst0 if not seen.setdefault(x[0], False) and not (seen.__setitem__(x[0], True))]
    return new_lst
