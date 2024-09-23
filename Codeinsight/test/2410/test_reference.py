import re

def test(string: str) -> list:
    return re.findall('\$(.*?)\$', string)

