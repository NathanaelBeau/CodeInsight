import re

def test(s: str) -> str:
    return re.sub(r'\d+$', '', s)
