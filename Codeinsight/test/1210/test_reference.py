def test(lst0):
    reversed_list = []
    for sublist in reversed(lst0):
        reversed_sublist = []
        for item in reversed(sublist):
            reversed_sublist.append(item)
        reversed_list.append(reversed_sublist)
    return reversed_list
