def test(str0):
    return [int(x) if '.' not in x else float(x) for x in str0.split(',')]

