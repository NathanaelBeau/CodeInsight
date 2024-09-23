def test(var1):
    return ''.join(c for i,c in enumerate(var1) if i%2==0)
