import re

def test(var0, var1):
    match = re.search(var1, var0)
    if match:
        return match.group(1)
    return None

