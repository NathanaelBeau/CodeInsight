def test(lst0):
    sorted_lst = sorted(lst0, key=lambda e: e['key']['subkey'], reverse=True)
    return sorted_lst