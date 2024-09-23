import re

def test(var0, lst0):
    pattern = r'(?i)\b(?:' + '|'.join(re.escape(item) for item in lst0) + r')\b'
    return re.findall(pattern, var0)

