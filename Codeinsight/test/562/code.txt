import re

def test(var0, var1):
    pattern = r'\b\d{{{0},}}\b'.format(var1)
    return re.findall(pattern, var0)
