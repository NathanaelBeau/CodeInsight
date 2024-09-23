def test(lst0):
    reversed_list = [list(reversed(sublist)) for sublist in reversed(lst0)]
    return reversed_list
