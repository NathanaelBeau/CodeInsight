import itertools
def test(lst0):
    def recursive_product(lsts, path=[]):
        if not lsts:
            yield tuple(path)
        else:
            for item in lsts[0]:
                yield from recursive_product(lsts[1:], path + [item])

    results = []
    for result_tuple in recursive_product(lst0):
       results.append(result_tuple)
    return results
