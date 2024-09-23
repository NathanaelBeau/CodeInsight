def test(var0, var1, lst0):
    str_lst = str(lst0)
    str_lst = str_lst.replace(str(var0), str(var1))
    return eval(str_lst)
