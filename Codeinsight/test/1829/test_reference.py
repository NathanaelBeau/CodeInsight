def test(str0, var0, var1):
    str_list = list(str0)
    str_list[var0] = var1
    return ''.join(str_list)

