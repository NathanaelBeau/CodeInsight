import itertools

def test(lst0):
    return sorted(set(itertools.chain.from_iterable(lst0)))

