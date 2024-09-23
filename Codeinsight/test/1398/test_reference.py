def test(s: str) -> [int, float]:
    try:
        return int(s)
    except ValueError:
        return float(s)