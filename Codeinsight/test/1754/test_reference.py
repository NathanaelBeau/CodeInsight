from itertools import repeat, chain

def test(str0, var0):
    return "".join(chain(*zip(*repeat(str0, var0))))
