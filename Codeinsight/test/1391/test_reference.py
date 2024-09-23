import re

def test(var0):
    pattern = r"lol+"
    match = re.match(pattern, var0)
    return bool(match)
