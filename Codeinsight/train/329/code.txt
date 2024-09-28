import re

def test(var0):
    pattern = r"^[a-zA-Z0-9]+$"
    return bool(re.match(pattern, var0))