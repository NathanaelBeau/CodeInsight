import re

def test_revised(var0, lst0):
    pattern = r'(?i)\b(?:' + '|'.join(re.escape(item) for item in lst0) + r')?\s?\d+(?:\.\d+)?'
    return re.findall(pattern, var0)
