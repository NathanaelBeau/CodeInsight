import re

def test(str0):
    numbers = ''.join(sorted(re.findall(r'\d', str0)))
    letters = ''.join(sorted(re.findall(r'[a-zA-Z]', str0)))
    
    return numbers + letters
