import re

def test(var0):
    pattern = r'\b[^\W\d_]+\b'  # This matches words, accounting for accent characters
    return re.findall(pattern, var0, re.UNICODE)

