def test(str0, var0):
    result = ""
    for i, char in enumerate(str0):
        if i % var0 == 0 and i != 0:
            result += " "
        result += char
    return result
