def test(lst0, lst1):
    return len([i for i, j in zip(lst0, lst1) if i != j])

