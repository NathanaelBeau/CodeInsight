def test(lst0: list) -> list:
    return [int(i) if isinstance(i, str) and i.isdigit() else i for i in lst0]

