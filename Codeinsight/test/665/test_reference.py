import re

def test(str0, var0):
    var0 = r'(\d+|\W+)'
    return [i for i in re.split(var0, str0) if i]


