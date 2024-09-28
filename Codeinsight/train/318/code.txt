def test(lst0):
    reversed_list = []
    for sub in lst0:
        reversed_list.append(sub[::-1])
    return reversed_list[::-1]