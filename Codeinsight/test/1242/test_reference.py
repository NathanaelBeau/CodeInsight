def test(lst0):
    filtered = sorted([x for x in lst0 if x > 2])
    return filtered[0] if filtered else None

