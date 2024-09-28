import re

def test(var0):
    pattern = r"(?P<repeat>.+?)\1+"
    return re.findall(pattern, var0, re.DOTALL)
