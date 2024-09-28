def test(lst0):
    if not lst0:
        return []

    num_columns = len(lst0[0])
    max_lengths = [0] * num_columns

    for row in lst0:
        for i, item in enumerate(row):
            max_lengths[i] = max(max_lengths[i], len(str(item)))

    return max_lengths
