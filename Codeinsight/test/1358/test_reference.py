def test(str0, lst0):
    lst0.append(str0)
    return sorted(lst0, key=lambda s: s.lower())

