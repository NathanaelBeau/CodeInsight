import re 

def test(var0):
    return re.sub(r'([a-z])\1+', r'\1', var0)