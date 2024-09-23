import re

def test(str0: str) -> str:
    return ''.join(re.findall(r'[^()]+(?![^(]*\))', str0))
