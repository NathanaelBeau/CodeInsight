import re

def test(var0):
    matches = re.findall(r'(?=(\d)(\d)\1\2)', var0)
    return [match[0] + match[1] for match in matches]
