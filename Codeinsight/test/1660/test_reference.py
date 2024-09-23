from itertools import chain

def test(dict0):
    mylist = list(chain.from_iterable(dict0.items()))
    return mylist
