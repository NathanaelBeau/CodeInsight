import re

def test(var0):
    return re.sub(r"(?<=\w)([A-Z])", r" \1", var0)
