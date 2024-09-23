def test(lst0):
    unique_data = list(map(list, set(map(lambda i: tuple(i), lst0))))
    sorted_data = sorted(unique_data)
    return sorted_data

