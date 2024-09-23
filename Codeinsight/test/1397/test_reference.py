import re

def test(str0: str, pattern: str) -> list:
    return re.split(pattern, str0)
