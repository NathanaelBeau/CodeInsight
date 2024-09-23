def test(lst0, var0):
    sorted_indices = sorted(range(len(lst0)), key=lambda i: lst0[i])
    return sorted_indices[-var0:]