import re

def test(str0):
     return ' '.join(word for word in str0.split() if not re.search(r'\d', word))


