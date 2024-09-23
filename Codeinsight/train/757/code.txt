import re

def test(var0):
    pattern = r'\[.*?\]|\(.*?\)|".*?"|\S+'
    return [match.group() for match in re.finditer(pattern, var0)]
