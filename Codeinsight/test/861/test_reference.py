

def test(a, var0=25, var1=100):
    return sum(1 for val in a if var0 < val <= var1)

