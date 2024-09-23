import string

def test(str0):
    out = str0.translate(str.maketrans('', '', string.punctuation))
    return out

