def test(lst0, *args):
    lengths = [len(lst0), *[len(arg) for arg in args]]
    return all(length == lengths[0] for length in lengths)
