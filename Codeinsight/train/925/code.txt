def test(lst0, var0):
    sublists = []
    index = 0
    while index < len(lst0):
        sublists.append(lst0[index:index+var0])
        index += var0
    return sublists
