def test(lst0):
    iseq = iter(lst0)
    first_type = type(next(iseq))
    return True if all( (type(x) is first_type) for x in iseq ) else False