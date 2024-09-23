import re

def test(str0: str) -> str:
    return re.sub(r'\(.*?\)', '', str0)
