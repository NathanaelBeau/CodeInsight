def test(lst0):
    for dct in lst0:
        if 'var0' in dct:
            del dct['var0']
    return lst0
