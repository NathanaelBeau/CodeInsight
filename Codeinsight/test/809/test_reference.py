def test(lst0: list) -> float:
    return sum(sum(i) for i in lst0) / sum(len(i) for i in lst0)