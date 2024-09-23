def test(lst0):
    lst0 = [word.lower() for word in lst0]
    return sorted(list(set(lst0)))
