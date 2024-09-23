def test(var0, var1, var2):
    start = var0.find(var1)
    while start >= 0 and var2 > 1:
        start = var0.find(var1, start+len(var1))
        var2 -= 1
    return start
