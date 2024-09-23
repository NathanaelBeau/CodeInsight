import re

def test(var0):
    pattern = "^(.+)\\n((?:\\n.+)+)"
    matches = re.findall(pattern, var0)
    return matches
