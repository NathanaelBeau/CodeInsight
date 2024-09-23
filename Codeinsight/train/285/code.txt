import re

def test(str0):
    return re.sub(r'[\W_]+', '', str0)
