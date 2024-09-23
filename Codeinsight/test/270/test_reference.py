def test(lst0, var0):
    for i in range(0, len(lst0), var0):
        yield lst0[i:i + var0]

