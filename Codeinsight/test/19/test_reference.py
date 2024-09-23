def test(lst0):
    return [x if x >= 10 else 'small' if x < 5 else 'medium' for x in lst0]
