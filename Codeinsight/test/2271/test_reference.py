import re

def test(str0, var0):
    return re.sub(".", lambda x: x.group() * var0, str0)
