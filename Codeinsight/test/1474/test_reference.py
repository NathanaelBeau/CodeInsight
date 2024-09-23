def test(str0, var0):
    result = ""
    for i in range(min(var0, len(str0))):
        result += str0[i]
    return result

