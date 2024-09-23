import re

def test(var0):
    match = re.match("(\d+(\.\d+)?)", var0)
    if match is None: 
        return None
    else:
        return match.group(1)
