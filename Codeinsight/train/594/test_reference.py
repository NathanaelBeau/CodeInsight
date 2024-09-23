def test(lst0):
    C = lst0[0].split(",")[1:-1]
    C1 = [float(i) for i in C if i]
    return C1

