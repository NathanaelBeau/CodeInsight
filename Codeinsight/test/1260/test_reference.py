from collections import OrderedDict

def test(lst0):
    d = OrderedDict()
    numbers = []

    for ni in lst0:
        if ni not in d:
            d[ni] = len(d)
        numbers.append(d[ni])

    return numbers
