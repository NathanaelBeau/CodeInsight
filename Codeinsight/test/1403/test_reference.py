import re

def test(var0, var1):
    return re.sub(r'\b\w\b', var1, var0)
 