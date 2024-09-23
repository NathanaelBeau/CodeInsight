import re

def test(str0):
    match = re.findall(r'(\S+)@', str0)
    if match:
        return match[0]
    else:
        return None

