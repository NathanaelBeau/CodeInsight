import re

def test(var0):
    return re.findall(r'(?<=\{)([^}]+)(?=\})', var0)

