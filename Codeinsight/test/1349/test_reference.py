import re

def test(str0):
    return [x.strip() for x in re.split(r'\s*,\s*', str0) if x.strip()]
