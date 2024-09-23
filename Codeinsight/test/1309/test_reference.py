def test(lst0):
    return [lst0[i] - lst0[i-1] for i in range(1, len(lst0))]

