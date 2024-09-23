def test(lst0):
    all_keys = set()
    for d in lst0:
        all_keys.update(d.keys())
    return all_keys

