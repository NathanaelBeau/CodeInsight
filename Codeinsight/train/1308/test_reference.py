import string

def test(var0):
    return ''.join(ch for ch in var0 if ch not in string.punctuation)