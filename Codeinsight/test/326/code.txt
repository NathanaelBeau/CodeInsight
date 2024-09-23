import re

def test(str0: str) -> str:
    return re.sub(r'\w+:\s?', '', str0)
