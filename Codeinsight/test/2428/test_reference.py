def test(lst0):
    unique_data = [list(x) for x in set(tuple(x) for x in lst0)]
    sorted_data = sorted(unique_data)
    return sorted_data

