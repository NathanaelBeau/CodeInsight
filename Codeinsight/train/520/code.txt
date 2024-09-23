def test(lst0):
    lst0.sort(key=lambda d: (d['weight'], d['factor']))
    return lst0
