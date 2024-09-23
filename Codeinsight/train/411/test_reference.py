def test(lst0: list, var0: str) -> dict:
    return next(item for item in lst0 if item["name"] == var0)

