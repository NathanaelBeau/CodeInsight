import re

def test(s: str) -> str:
    return re.sub("[^0-9a-zA-Z]", "", s)
