def test(lst0, var0, var1):
    my_dict = dict((k, []) for k in lst0)
    my_dict[var0].append(var1)
    return my_dict
