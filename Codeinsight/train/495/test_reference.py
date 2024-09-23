import re

def test(str0, str1):
    return [m.start() for m in re.finditer(str0, str1)]

