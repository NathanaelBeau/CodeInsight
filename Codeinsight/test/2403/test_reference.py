def test(str0, var0, str1):
    padding = max(0, var0 - len(str0))
    left_padding = [str1] * (padding // 2)
    right_padding = [str1] * (padding - len(left_padding))
    return ''.join(left_padding) + str0 + ''.join(right_padding)
