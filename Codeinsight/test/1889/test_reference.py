import re

def test(var0):
    return re.sub(r'([A-Z])\1+', lambda m: m.group(1).lower(), var0)

