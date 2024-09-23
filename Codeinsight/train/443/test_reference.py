import re

def test(var0):
    return re.findall(r'(less than \d+|greater than \d+|between \d+ and \d+|more than \d+|\d+(?:\.\d+)?(?:\s?-\s?\d+(?:\.\d+)?)?)', var0)
