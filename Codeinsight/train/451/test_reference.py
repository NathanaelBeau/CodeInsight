import re

def test(var0):
    return re.sub(r'(?P<ch>.)', lambda m: str(ord(m.group('ch'))), var0)
