def test(lst0):
    return [item for sublist in lst0 for item in (test(sublist) if isinstance(sublist, list) else [sublist])]
