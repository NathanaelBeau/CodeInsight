def test(lst0, index):
    return [lst0[i] for i, _ in enumerate(lst0) if i in index]
