import re

def test(var0):
    lst = re.split(',', var0)
    return ['0' if x == '' else x for x in lst]