import re

def test(str0):
    return re.sub(r'\b(.+)\s+\1\b', r'\1', str0)

