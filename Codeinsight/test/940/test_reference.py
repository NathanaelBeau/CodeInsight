def test(lst0):
    return sorted((sorted(item) for item in lst0), key=lambda x: (len(x), x))

