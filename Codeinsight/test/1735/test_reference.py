import re

def test(str0):
    return re.findall(r'\b\w+\b', str0)
