import re

def test(str0):
    return re.match(r'(?:.*?[A-Z]){3}.*?([A-Z].*)', str0).group(1)
