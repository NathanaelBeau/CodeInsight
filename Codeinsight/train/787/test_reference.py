def test(lst0: list) -> int:
    return sum(sum(sublist) for sublist in lst0)