def test(lst0):
    return max(enumerate(lst0), key=lambda x: x[1])[0]
