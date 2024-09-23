def test(lst0):
    return [x for x in lst0 if not any(c.isdigit() for c in x)]
