def test(lst0):
    lst0.sort(key=lambda e: e['key']['subkey'], reverse=True)
    return lst0
