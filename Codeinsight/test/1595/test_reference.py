import re
def test(str0):
    return re.sub(r'[^a-zA-Z0-9]', '', str0)