def test(lst0):
    return sorted(lst0, key=lambda x: int(x.split('.')[2]))

