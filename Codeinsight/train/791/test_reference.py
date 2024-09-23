def test(lst0):
    for item in lst0:
        if lst0.count(item) > 1:
            return False
    return True

