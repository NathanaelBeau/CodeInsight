def test(lst0):
    lst0.sort(key=lambda x: sum(y['play'] for y in x), reverse=True)
    return lst0
