import re
def test(var0):
    return re.sub(r'\bget\b', 'get@', var0)