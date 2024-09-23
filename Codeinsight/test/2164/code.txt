import re

def test(s: str) -> list:
    return re.split(r'(\s+)', s)