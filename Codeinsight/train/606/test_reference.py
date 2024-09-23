def test(lst0):
    reversed_tuples = []
    for x in lst0:
        reversed_tuple = tuple(reversed(x))
        reversed_tuples.append(reversed_tuple)
    return tuple(reversed_tuples)
