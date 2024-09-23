import re

def test(str0):
    return re.sub(r'\.(?=[^ .])', '. ', str0)

