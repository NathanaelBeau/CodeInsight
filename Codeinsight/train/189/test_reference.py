def test(var1, var2):
    smaller = var1 if var1 < var2 else var2
    for i in range(1, smaller+1):
        if (var1 % i == 0) and (var2 % i == 0):
            hcf = i
    return hcf