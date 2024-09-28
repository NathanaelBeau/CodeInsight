def test(lst0):
    seen = set()
    new_list = []
    for sublist in lst0:
        tuple_sublist = tuple(sublist)
        if tuple_sublist not in seen:
            seen.add(tuple_sublist)
            new_list.append(sublist)
    return new_list
