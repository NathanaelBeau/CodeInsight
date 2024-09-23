import re

def test(str0: str) -> list:
    return [x for x in re.split(r'(\W+)', str0) if x]
