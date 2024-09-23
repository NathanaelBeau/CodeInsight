import re

def test(var0, var1, var2, var3):
    where = [m.start() for m in re.finditer(var1, var3)][var0-1]
    before = var3[:where]
    after = var3[where:]
    newString = before + after.replace(var1, var2, 1)
    return newString
