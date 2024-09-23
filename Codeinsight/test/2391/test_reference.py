import re

def test(var0):
    pattern = r'\b\w*[\u00C0-\u017F]\w*\b'
    return re.findall(pattern, var0)
