import re

def test(str0):
    pattern = re.compile(r"(.+?)\1+")
    return [match.group(0) for match in pattern.finditer(str0)]

