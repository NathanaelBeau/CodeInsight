import re

def test(var0):
    return re.sub(r'(\w+)\s+\1', r'\1', var0)
