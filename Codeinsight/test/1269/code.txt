import re

def test(var0, var1):
    return re.findall(r'^' + var1 + r'$', var0)
