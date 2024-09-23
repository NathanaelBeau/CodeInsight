def test(var0, var1, var2, var3):
    inds = [i for i in range(len(var3) - len(var1)+1) if var3[i:i+len(var1)]==var1]
    var3 = list(var3)
    var3[inds[var0-1]:inds[var0-1]+len(var1)] = var2
    return ''.join(var3)