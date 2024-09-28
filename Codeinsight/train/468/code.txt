def test(lst0, lst1):
    len_min = min(len(lst0), len(lst1))
    for i in range(len_min):
        if lst0[i] >= lst1[i]:
            return False
    return True
