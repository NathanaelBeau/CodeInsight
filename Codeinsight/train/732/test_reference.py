import re

def test(str0):
    return re.split(r'[;,\s]\s*', str0)
