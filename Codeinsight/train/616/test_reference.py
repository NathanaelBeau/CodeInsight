import string

def test(str0):
    translator = str0.maketrans("", "", string.punctuation)
    return str0.translate(translator)
