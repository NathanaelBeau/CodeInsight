import re
def test(lst0):
    result = any(re.search(r'\d', s) for s in lst0)
    return result