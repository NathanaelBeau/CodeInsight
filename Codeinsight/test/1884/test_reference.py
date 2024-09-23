import re
def test(var0):
    return re.sub(r'\s+([.,!?;:])', r'\1', var0)

