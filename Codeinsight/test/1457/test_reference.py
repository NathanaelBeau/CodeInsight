def test(dict0):
    lst = []
    for key, value in dict0.items():
        lst.extend([key, value])
    return lst