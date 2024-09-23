def test(lst0):
    return list(map(lambda x: x[0], filter(lambda x: x[1][0] == 53, enumerate(lst0))))
