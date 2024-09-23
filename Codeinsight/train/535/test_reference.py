def test(lst0, lst1, var0):
    order_dict = {color: index for index, color in enumerate(lst0)}
    lst1.sort(key=lambda x: order_dict[x[var0]])
    return lst1

