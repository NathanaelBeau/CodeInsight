import re

def test(str0):
    return ''.join(re.findall(r'[A-Z][^A-Z]*', str0)[3:])

