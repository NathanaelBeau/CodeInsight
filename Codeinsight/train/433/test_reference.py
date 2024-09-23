import re
def test(str0):
    return re.findall(r'[A-Z][^A-Z]*', str0)
