def test(lst0, lst1, var0):
    return [x for x in lst0 if x not in lst1][:var0]
