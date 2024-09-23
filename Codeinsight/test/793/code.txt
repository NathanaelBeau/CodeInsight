import re

def test(str0):
    return re.findall(r'\S+', str0)
