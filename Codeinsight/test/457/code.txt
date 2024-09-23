from itertools import groupby

def test(lst0):
    result = []
    for _, group in groupby(lst0):
        result.extend([list(group)])
    return result
