import re

def test(var0, var1):
    return [m.start() for m in re.finditer(var0, var1)]
