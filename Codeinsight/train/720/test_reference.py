import re

def test(var0):
    return [part for part in re.split(r'\D+', var0) if part]

