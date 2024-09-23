import re

def test(var0):
    return re.sub(r'^[^\x00-\x7F]+|[^\x00-\x7F]+$', '', var0)

