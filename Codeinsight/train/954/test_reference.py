from functools import reduce

def test(str0):
    return reduce(lambda acc, char: char + acc, str0, "")
