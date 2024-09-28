import itertools

def test(lst0, lst1):
    return zip(lst0, itertools.cycle(lst1)) if len(lst0) > len(lst1) else zip(itertools.cycle(lst0), lst1)