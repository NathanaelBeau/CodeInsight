import re

def test(lst0):
    return sorted(lst0, key=lambda x: int(re.search(r'(\d+)$', x).group()))
