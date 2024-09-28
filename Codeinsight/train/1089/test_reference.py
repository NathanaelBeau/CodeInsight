def test(str0, var0, str1):
    padding = (var0 - len(str0)) // 2
    left_padding = str1 * padding
    right_padding = str1 * (var0 - len(str0) - padding)
    return left_padding + str0 + right_padding
