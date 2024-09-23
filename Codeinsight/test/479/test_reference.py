def test(str0,var0, var1):
    original_char = str0[var0]
    return str0[:var0] + str0[var0:].replace(original_char, var1, 1)
