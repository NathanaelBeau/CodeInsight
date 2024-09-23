def test(lst0, lst1):
    return [dict for dict in lst0 if dict['link'] not in lst1]

