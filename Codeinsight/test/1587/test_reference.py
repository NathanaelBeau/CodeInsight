import re

def test(var0, var1):
    matches = re.findall(var1, var0)
    return [match[::-1] for match in matches]

