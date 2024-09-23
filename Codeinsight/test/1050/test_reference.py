import re

def test(var0, var1):
    match = re.match(var1 + r'$', var0)
    if match:
        return [match.group()]
    return []
