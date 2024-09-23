def test(lst0, *args):
    lengths = [len(lst0), *map(len, args)]
    return all(length == lengths[0] for length in lengths)