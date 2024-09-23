import re
def test(var0):
    return re.sub(r'(?<=[a-z])([A-Z])', r'-\1', var0).lower()

