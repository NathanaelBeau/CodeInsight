def test(lst0):
    temp_list = []
    for item in lst0:
        temp_list.append(float(item))
    temp_list.sort()
    return [str(item) for item in temp_list]
