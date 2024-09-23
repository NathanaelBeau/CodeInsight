import re

def test(var0):
    return re.sub(r"(?<=[a-z])\r?\n"," ", var0)
