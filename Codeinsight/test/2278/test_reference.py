import re

def test(s: str) -> str:
    return re.sub(r'\((\w+)\)', r'\1', s)
