import re

def test(str0: str) -> list:
    return re.findall(r'[A-Z][^A-Z]*', str0)
