def test(lst0):
    idx = sorted(range(len(lst0)), key=lst0.__getitem__)
    ridx = sorted(range(len(lst0)), key=idx.__getitem__)
    return ridx

