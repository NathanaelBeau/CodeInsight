def test(lst0: list, lst1: list) -> bool:
    return all(i < j for i, j in zip(lst0, lst1))

