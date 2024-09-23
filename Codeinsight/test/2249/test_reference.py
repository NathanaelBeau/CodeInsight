import re

def test(str0):
    m = re.search(r"//([^/]*)", str0)
    if m:
        return m.group(1)
    else:
        return None

