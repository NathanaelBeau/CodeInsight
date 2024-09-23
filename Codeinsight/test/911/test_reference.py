from functools import reduce
def test(var0, lst0):
    return reduce(lambda l, e: l+var0*[e], lst0, [])

