def test(lst0: list) -> list:
    return [item for item in lst0 if sum(item) > 10]
