def test(lst0, dict0):
    return [[item for _, item in sorted(zip(map(dict0.get, item), item))] for item in lst0]

