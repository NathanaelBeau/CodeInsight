def test(lst0):
    flattened_list = [item for tpl in lst0 for item in tpl]
    return flattened_list
