import re

def test(str0):
    p = re.compile(r'((?:Friday|Saturday)\s*\d{1,2})')
    return re.split(p, str0)

