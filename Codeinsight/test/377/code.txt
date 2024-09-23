def test(lst0):
    seen = set()
    for x in lst0:
        if x in seen:
            return False
        seen.add(x)
    return True
