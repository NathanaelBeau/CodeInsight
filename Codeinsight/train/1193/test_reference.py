import re

def test(str0):
    words = re.findall(r'\b[^\d\W]+\b', str0)
    return len(words)