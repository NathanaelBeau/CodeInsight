import re

def test(str0, var0):
    match = re.search(var0, str0)
    if match:
        return match.start()
    else:
        return -1

