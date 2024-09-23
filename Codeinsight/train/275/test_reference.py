import re

def test(str0):
    return re.sub(r'\w*\d\w*', '', str0).strip()

