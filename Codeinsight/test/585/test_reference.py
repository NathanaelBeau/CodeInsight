from itertools import islice

def test(lst0):
    iterator = islice(lst0, 10)
    result = [item for item in iterator]
    return result
