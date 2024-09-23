def test(lst0, lst1):
    sorted_indices = sorted(range(len(lst0)), key=lambda k: lst0[k])
    sorted_lst0 = [lst0[i] for i in sorted_indices]
    sorted_lst1 = [lst1[i] for i in sorted_indices]
    return tuple(sorted_lst0), tuple(sorted_lst1)
