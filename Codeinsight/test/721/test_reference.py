def test(lst0, lst1):
    result = [item for sublist in [lst1, lst0] for item in sublist]
    return result
