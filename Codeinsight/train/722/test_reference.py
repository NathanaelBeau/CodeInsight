import itertools

def test(dict0):
    return list(itertools.chain(*[[k] * v for k, v in dict0.items()]))
