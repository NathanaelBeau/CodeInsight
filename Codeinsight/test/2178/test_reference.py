import itertools

def test(lst0, var0):
    result = []
    for combination in itertools.permutations(lst0, var0):
        result.append(''.join(combination))
    return result

