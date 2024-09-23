import re

def test(str0):
    pattern = "([0-9]+)([A-Z])"
    return re.findall(pattern, str0)

