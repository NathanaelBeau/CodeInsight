import re

def test(var0):
    match = re.search(r'\[(.*?)\]', var0)
    return match.group(1) if match else None
