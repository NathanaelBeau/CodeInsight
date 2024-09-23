import re

def test(var0):
    return bool(re.search(r'[^\x00-\x7F]+', var0))