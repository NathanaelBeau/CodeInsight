import re
def test(var0, dict0):
    pattern = r'\b(?:' + '|'.join(re.escape(key) for key in dict0.keys()) + r')\b'
    return re.sub(pattern, lambda m: dict0[m.group(0)], var0)
