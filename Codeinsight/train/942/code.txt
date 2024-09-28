def test(x: list) -> list:
    return max(x, key=sum)
