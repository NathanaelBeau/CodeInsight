def test(lst0: list) -> list:
    return [s.rstrip("\r\n") for s in lst0]
