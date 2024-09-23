import re

def test(str0, pat0, str1, bool0) -> str:
    if bool0:
        return re.sub(pattern, replacement, str0, flags=re.I)
    return re.sub(pattern, replacement, str0)
