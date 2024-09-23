def test(lst0, length, fill_value):
    for sublist in lst0:
        while len(sublist) < length:
            sublist.append(fill_value)
    return lst0

