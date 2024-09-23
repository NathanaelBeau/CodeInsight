import re

def test(var0, var1, str0):
    pattern = re.compile(var0)
    return pattern.sub(var1, str0)

