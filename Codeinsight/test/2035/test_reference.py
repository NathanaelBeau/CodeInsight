import re

def test(str0: str, pattern: str) -> list:
    return re.findall(pattern, str0)
