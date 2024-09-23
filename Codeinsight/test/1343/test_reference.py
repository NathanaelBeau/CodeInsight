def test(str0):
    reversed_str = ""
    for i in range(len(str0) - 1, -1, -1):
        reversed_str += str0[i]
    return reversed_str

