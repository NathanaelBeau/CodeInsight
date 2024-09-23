import re

def test(lst0, var0):
    result = any(re.search(var0, s) for s in lst0)
    return result