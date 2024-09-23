import re

def test(str0, var0, var1):
    pattern = re.escape(var1) + '+(' + re.escape(var0) + ')'
    match = re.search(pattern, str0)
    return match.group(1) if match else None

