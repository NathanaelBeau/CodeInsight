import re

def test(str0):
    return re.sub(r"^\s+", "", str0, flags=re.MULTILINE)