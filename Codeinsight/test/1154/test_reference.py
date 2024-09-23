def test(str0, str1):
    for var0 in range(len(str1) - len(str0) + 1):
        if str1[var0:var0 + len(str0)] == str0:
            return var0
    return -1
