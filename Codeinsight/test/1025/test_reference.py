import re

def test(var0,str0):
    matches = re.findall(var0, str0)
    count0 = len(matches)
    return count0