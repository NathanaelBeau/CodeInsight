import re

def test(str0):
    return re.sub(r'\b\d+\b', '', str0)