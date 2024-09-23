def test(lst0):
    d = {}
    for item in lst0:
        key = item[:5]
        d.setdefault(key, []).append(item)
    return list(d.values())
