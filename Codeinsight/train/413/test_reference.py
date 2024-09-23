def test(functions: list, values: list) -> list:
    return [[func(val) for func in functions] for val in values]

