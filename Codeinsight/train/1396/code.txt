import re

def test(str0, var0):
    return [m.group(0) for m in re.finditer(str0, var0, re.IGNORECASE)]
