import itertools

def test(dict0):
    bl = [[k, v] for k, v in dict0.items()]
    return list(itertools.chain(*bl))
