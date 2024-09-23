def test(dict0, lst0):
    return {x: dict0[x] for x in lst0 if x in dict0}
