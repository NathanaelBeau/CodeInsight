import itertools

def test(lst0, var0):
    result = [''.join(combination) for combination in itertools.permutations(lst0, var0)]
    return result
