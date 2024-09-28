import re

def test(str0, pattern):
    return re.findall(pattern, str0)