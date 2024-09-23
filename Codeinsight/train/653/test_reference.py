import itertools

def test(lst0):
    groups = [list(g) for _, g in itertools.groupby(lst0, lambda x: x.split('_')[0])]
    return groups

