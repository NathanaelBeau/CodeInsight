def test(a: str) -> bool:
    try:
        int(a)
        return True
    except ValueError:
        return False
