import re

def test(var0):
    return ' '.join([word.title() if re.search(r'\w', word) else word for word in var0.split()])

