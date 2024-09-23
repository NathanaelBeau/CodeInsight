import re

def test(str0: str) -> str:
    return re.sub(r'[^a-zA-Z0-9]', '', str0)
