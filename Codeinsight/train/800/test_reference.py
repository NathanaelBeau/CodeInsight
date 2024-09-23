def test(lst0):
    try:
        return min(x for x in lst0 if x > 2)
    except ValueError:
        return None

