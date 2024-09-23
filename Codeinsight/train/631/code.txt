def test(lst0):
    result = ""
    for elem in lst0:
        result += elem[0] + "\n"
    return result.rstrip("\n")
