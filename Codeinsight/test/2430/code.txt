def test(lst0, lst1):
    if lst1 is None:
        lst1 = []

    sorted_strings = []

    for index, s in enumerate(lst0):
        if index in lst1:
            sorted_strings.append(''.join(sorted(s, reverse=True)))
        else:
            sorted_strings.append(''.join(sorted(s)))

    return sorted_strings