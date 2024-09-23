import re

def test(str0):
    match = re.search(r'\[(\d+)\]', str0)
    return match.group(1) if match else None
