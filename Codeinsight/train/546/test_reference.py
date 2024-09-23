def test(lst0):
    m = max(lst0)
    return [i for i, j in enumerate(lst0) if j == m]

