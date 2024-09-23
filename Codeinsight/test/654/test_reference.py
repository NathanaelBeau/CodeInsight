import string

def test(str0):
    return str0.translate(str.maketrans('', '', string.punctuation))
