def test(lst0, dict0, var0):
    sorted_dict = []
    id_index_map = {d[var0]: i for i, d in enumerate(dict0)}
    for id in lst0:
        if id in id_index_map:
            sorted_dict.append(dict0[id_index_map[id]])
    return sorted_dict