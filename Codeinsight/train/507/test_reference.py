import re

def test(str0):
    return re.sub(r"(\d+)", r'"\1"', str0)

