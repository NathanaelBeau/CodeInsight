import re
def test(str0):
    return re.sub('\u200b', '*', str0)

