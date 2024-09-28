import re

def test(var0):
    pattern = r',(?=(?:[^"]*"[^"]*")*[^"]*$)'
    return re.split(pattern, var0)