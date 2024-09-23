import re

def test(var0):
    match = re.search(r'a+(b)', var0)
    return match.group(1) if match else None
