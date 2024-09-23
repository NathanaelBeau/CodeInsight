def test(var1):
    r = range(1, var1)
    a = sum(r)
    return a * a - sum(i*i for i in r)