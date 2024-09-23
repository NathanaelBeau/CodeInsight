def test(str0):
    result = ""
    for i in range(0, len(str0), 2):
        if i + 1 < len(str0):
            result += str0[i + 1] + str0[i]
        else:
            result += str0[i]
    return result
