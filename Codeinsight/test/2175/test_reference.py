import re

def test(str0):
    return re.sub(r'[^\w\s]', '', str0)
