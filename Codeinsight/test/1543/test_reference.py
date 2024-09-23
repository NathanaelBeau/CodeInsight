import itertools

def test(sublist):
    return list(itertools.chain.from_iterable(sublist))
