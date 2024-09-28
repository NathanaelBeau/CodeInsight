import re

def test(str0):
    return re.sub(r"[0-9]", "", str0)
