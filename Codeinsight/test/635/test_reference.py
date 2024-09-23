def test(s: str) -> str:
    return ''.join('{:02x}'.format(ord(c)) for c in s)

