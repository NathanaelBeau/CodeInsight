def test(str0,var0, var1):
    original_char = str0[var0]
    translation_table = str.maketrans(original_char, var1)
    return str0[:var0] + str0[var0:].translate(translation_table)[:1] + str0[var0+1:]


