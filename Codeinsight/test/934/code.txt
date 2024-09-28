import string

def test(str0):
    for c in string.punctuation:
        str0 = str0.replace(c, "")
    return str0

