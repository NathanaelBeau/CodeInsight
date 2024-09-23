import re

def test(lst0):
    return [re.sub(r"\s+\(\w+\)", "", item) for item in lst0]

