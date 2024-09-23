def test(s: str) -> [int, float]:
    return int(s) if "." not in s else float(s)

