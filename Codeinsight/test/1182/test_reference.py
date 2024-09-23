import re

def test(str0, var0):
    p = re.compile(var0)
    return re.split(p, str0)

