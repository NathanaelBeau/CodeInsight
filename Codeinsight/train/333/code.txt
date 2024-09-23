def test(var0):
    if var0 == 0:
        return '0'
    n, res = abs(var0), ''
    while n:
        res = str(n % 7) + res
        n //= 7
    return res if var0 > 0 else '-' + res
