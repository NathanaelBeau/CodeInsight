import re

def test(str0, var0):
    sentences = re.split(r'(?<=[.?!])\s+', str0)
    if len(sentences) > var0:
        return ' '.join(sentences[:var0])
    else:
        return str0
