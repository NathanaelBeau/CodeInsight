import re

def test(var0, lst0):
    pattern = r'({})'.format('|'.join(map(re.escape, lst0)))
    match = re.search(pattern, var0)
    return match.group(0) if match else None

