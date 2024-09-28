import re

def test(var0, exceptions='', replacement=''):
    pattern = r'[^a-zA-Z0-9' + re.escape(exceptions) + r']'
    return re.sub(pattern, replacement, var0)
