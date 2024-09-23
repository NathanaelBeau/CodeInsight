def test(var1,var2):
    bigger = var1 if var1 > var2 else var2
    while True:
        if (bigger % var1 == 0) and (bigger % var2 == 0):
            break
        bigger += 1
    return bigger