import re

def test(str0, var0):
    return re.findall(str0, var0, re.IGNORECASE | re.MULTILINE)
