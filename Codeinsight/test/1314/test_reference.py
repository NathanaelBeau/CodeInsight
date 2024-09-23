import re
def test(var0, var1, var2):
    return re.sub(var1, lambda m: m.group(0) + var2, var0)
