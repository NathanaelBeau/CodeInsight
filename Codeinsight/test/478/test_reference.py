import re

def test(str0):
    pattern = r"'(''|[^'])*'"
    matches = re.findall(pattern, str0)
    return matches
