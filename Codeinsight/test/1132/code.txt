import re

def test(var0):
    return re.findall(r'(.)\1+', var0)
