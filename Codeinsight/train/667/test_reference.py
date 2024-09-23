import re

def test(str0):
    return [re.split(r'\t', row) for row in re.split(r'\n', str0)]

