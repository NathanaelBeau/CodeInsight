import re

def test(var0, pattern):
    matches = re.findall(pattern, var0)
    return matches[-1] if matches else None

