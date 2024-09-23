def test(var0):
    int_part = format(int(var0), ',').replace(',', ' ')
    dec_part = format(var0, '.2f').split('.')[1]
    return int_part + ',' + dec_part if int(var0) >= 1000 else str(var0).replace('.', ',')
