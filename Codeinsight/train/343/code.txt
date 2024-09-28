import re

def test(str0, var0):
    return re.sub(r'^.*?' + re.escape(var0), var0, str0)
