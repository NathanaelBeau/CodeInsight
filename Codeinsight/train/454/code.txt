import re
def test(var0):
    pattern = r'\b(\w+)\b(?=.*\b\1\b)'
    return re.findall(pattern, var0)
