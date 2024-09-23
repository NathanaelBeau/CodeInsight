import re

def test(s):
    return re.sub(r'\d+$', '', s)