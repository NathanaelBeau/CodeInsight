def test(var1,var2,var3):
    if var1 > 0 and var2 > 0 and var3 > 0:
        if var1 + var2 > var3 and var1 + var3 > var2 and var2 + var3 > var1:
            return True
    return False