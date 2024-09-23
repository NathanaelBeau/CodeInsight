import re

def test(str0: str, pattern: str, replacement: str) -> str:
    return re.sub(pattern, replacement, str0)

