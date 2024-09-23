def test(str0):
    decimal_index = str0.find('.')
    if decimal_index != -1:
        int_part = str0[:decimal_index]
        return int(int_part)
    else:
        return int(str0)

