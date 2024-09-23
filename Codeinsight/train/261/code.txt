import re

def test(str0):
    pattern = r'\d+'
    result = [int(match) for match in re.findall(pattern, str0)]
    return result