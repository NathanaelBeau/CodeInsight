def test(lst0):
    return list(map(lambda s: sum(map(int, filter(str.isdigit, s))), lst0))
