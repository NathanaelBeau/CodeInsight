import re

def test(var0):
    return re.sub(r'[^a-zA-Z0-9 ]', '', var0)
