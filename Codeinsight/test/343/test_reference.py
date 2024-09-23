def test(lst0):
    C = lst0[0].split(",")[1:-1]
    C1 = list(map(float, filter(lambda x: x.strip(), C)))
    return C1

