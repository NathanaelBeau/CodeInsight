def test(s: str) -> str:
    while s and s[-1].isdigit():
        s = s[:-1]
    return s
