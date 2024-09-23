import re

def test(str0: str) -> list:
    return re.findall(r'\w+|\W+', str0)

