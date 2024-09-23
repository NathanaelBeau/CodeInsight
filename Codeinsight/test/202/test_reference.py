import re

def test(mystring, var0, var1):
    pattern = r"{}{}{}".format(var1, var0, var1)
    return re.findall(pattern, mystring)
