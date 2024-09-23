def test(lst0, lst1):
    for item in lst0:
        if item not in lst1:
            return False
    return True
