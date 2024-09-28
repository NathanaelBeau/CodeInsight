def test(dict0, var0):
    sorted_items = sorted(dict0.items(), key=lambda item: item[1][var0])
    return list(map(lambda item: item[0], sorted_items))