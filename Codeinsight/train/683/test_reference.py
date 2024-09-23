def test(lst0):
    lst0.reverse()
    for sublist in lst0:
        sublist.reverse()
    return lst0
