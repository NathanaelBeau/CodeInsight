import re

def test(var0, var1):
    match = re.search(var0, var1)
    if match:
        return match.group(0)
    else:
        return None
