import re

def test(lst0):
    return [x for x in lst0 if not re.search(r'\d', x)]