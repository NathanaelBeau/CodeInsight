import re

def test(str0):
    match = re.search(r'\?+$', str0)
    return len(match.group()) if match else 0
