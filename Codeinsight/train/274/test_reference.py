def test(str0, var0, var1):
    trans_table = str0.maketrans(var0, var1)
    return str0.translate(trans_table)
