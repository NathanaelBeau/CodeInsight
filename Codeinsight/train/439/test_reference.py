import re

def test(str0, var0):
    return [match for match in re.findall(str0, var0, re.IGNORECASE)]