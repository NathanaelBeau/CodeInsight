def test(str0, lst0):
    start, stop = map(int, str0.split(':'))
    return lst0[start:stop]
