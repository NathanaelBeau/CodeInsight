import re

def test(str0: str, pattern: str) -> list:
    return [match.group() for match in re.finditer(pattern, str0)]
