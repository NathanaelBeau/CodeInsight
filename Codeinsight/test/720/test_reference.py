def test(a: list, index: int) -> list:
    return a[:index] + a[index+1:]
