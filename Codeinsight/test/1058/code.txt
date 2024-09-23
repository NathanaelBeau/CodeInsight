def test(lst0):
    reversed_tuples = []
    for x in lst0:
        reversed_tuple = ()
        for item in x:
            reversed_tuple = (item,) + reversed_tuple
        reversed_tuples.append(reversed_tuple)
    return tuple(reversed_tuples)
