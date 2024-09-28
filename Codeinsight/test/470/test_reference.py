def test(lst0, key0, value0):
    return next((item for item in lst0 if item.get(key0) == value0), None)
