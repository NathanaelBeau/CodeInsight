import re

def test(str0):
    return re.sub(r'\u200b', '*', str0)

