def test(lst0: list, lst1: list) -> list:
    return [x for x in lst0 if lst0.count(x) >= 1 and lst1.count(x) >= 1]
