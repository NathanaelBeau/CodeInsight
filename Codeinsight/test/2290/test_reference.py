import re

def test(var0, var1):
    return re.findall(r'(?=({}[a-zA-Z]*))'.format(var1), var0)

