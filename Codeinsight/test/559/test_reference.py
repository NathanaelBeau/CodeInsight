def test(lst0, var0):
    sorted_indexes = sorted(range(len(lst0)), key=lambda index: lst0[index][var0], reverse=True)
    return sorted_indexes[0]

