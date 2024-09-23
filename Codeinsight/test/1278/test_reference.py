from string import digits

def test(str0: str) -> str:
    return ''.join(c for c in str0 if c in digits)
