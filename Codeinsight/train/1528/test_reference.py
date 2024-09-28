def test(lst0):

    def get_subkey(e):
        return e['key']['subkey']

    sorted_lst = sorted(lst0, key=get_subkey, reverse=True)
    return sorted_lst
