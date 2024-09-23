import re

def test(var0, pattern):
    return re.search(pattern, var0).group(0)
