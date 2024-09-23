import re

def test(lst0):
    return [re.split(r"_(?:f?or|and)_", s) for s in lst0]
