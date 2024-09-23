def test(var0):
    lst = var0.split(",")
    return ['0' if x == '' else x for x in lst]

