def test(lst0, var0):
    take_closest = lambda num, collection: min(collection, key=lambda x: abs(x - num))
    return take_closest(var0, lst0)

