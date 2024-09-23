def test(lst0):
    integer_list = []
    for s in lst0:
        total = 0
        for char in s:
            if char.isdigit():
                total += int(char)
        integer_list.append(total)
    return integer_list
