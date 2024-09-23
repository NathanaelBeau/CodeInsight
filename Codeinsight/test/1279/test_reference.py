import sys

def test(s: str) -> int:
    return sys.getsizeof(s.encode('utf-8')) - 33