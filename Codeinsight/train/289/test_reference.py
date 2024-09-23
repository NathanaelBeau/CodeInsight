import re

def test(str0):
    return re.sub("[^0-9]", "", str0)
