import re

def test(str0):
    return [i.split() for i in re.findall(r'\[([^\[\]]+)\]', str0)]

