import re

def test(str0, var0, var1, bool0):
    flags = re.IGNORECASE if bool0 else 0
    return re.sub(var0, var1, str0, flags=flags)