import re

def test(str0: str) -> list:
    return re.split(r'(\s+)', str0)