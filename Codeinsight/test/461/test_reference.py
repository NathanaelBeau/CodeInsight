import re
def test(var0, var1, var2):
    matches = [m.start() for m in re.finditer(var1, var0)]
    if len(matches) < var2:
        return -1
    return matches[var2 - 1]

