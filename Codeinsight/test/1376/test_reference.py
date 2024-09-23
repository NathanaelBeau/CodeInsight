import re

def test(str0):
    return re.sub(r" \(\w+\)", "", str0)

