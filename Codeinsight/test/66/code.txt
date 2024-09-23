import re

def test(str0):
    match = re.match(r'^\d+$', str0)
    return int(match.group()) if match else None