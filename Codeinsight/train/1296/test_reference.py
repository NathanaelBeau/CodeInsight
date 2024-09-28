def test(lst0, var0):
    my_dict = dict((k, []) for k in lst0)
    my_dict[var0].append(1)
    return my_dict