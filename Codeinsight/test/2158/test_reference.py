def test(lst0, num0):
    return min(lst0, key=lambda x: abs(x - num0))
