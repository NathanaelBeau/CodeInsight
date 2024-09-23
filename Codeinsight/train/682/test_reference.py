import re

def test(str0):
    splitter = re.compile(r'(\s+|\S+)')
    return splitter.findall(str0)

