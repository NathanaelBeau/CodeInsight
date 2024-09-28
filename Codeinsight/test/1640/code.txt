import re

def test(str0, pat0, str1, bool0):
    flags = re.IGNORECASE if bool0 else 0
    return re.sub(pat0, str1, str0, flags=flags)