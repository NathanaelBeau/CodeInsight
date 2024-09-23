import re

def test(s):
    return re.sub(r'\((\w+)\)', r'\1', s)

