def test(lst0):
    return sorted(lst0, key=lambda item: (-len(item), item))
