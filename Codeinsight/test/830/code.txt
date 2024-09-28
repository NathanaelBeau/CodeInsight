def test(var0, var1, var2):
    index = var0.find(var1)
    if index == -1:
        return var0
    else:
        if var1[0].isupper():
            return var0[:index] + var2.capitalize() + var0[index + len(var1):]
        else:
            return var0[:index] + var2 + var0[index + len(var1):]
