def test(lst0, var0):
    return sorted(range(len(lst0)), key=lambda i: lst0[i])[-var0:]
