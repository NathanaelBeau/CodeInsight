def test(var1, var2):
    if var2 == 1 and var1 != 1:
        return False
    if var2 == 1 and var1 == 1:
        return True
    if var2 == 0 and var1 != 1:
        return False
    power = int (math.log(var1, var2) + 0.5)
    return var2 ** power == var1