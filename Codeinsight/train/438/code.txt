import re

def test(str0, var0):
    pattern = re.compile(str0, re.IGNORECASE | re.MULTILINE)
    return pattern.findall(var0)