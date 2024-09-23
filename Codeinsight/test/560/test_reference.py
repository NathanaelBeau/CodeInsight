def test(lst0, var0):
    return max(enumerate(lst0), key=lambda arg: arg[1][var0])[0]

