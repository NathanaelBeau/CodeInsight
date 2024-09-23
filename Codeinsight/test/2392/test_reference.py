import re

def test(var0):
    pattern = r"(?<![0-9])[0-9]{2}(?![0-9])"
    return re.findall(pattern, var0)

