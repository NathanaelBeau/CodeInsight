def test(lst0):
    from functools import reduce
    result = reduce(lambda a, b: {**a, **b}, lst0)
    return result
