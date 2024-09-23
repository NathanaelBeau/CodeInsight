import re

def test(lst0, var0):
    return [item for item in lst0 if not re.search(var0, item)]

