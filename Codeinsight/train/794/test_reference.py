def test(str0: str) -> str:
    if not str0:
        return str0
    return str0[0].swapcase() + str0[1:]
