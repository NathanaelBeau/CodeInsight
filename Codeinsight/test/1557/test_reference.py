def test(lst0):
    lst0.sort(key=lambda item: (-len(item), item))
    return lst0

