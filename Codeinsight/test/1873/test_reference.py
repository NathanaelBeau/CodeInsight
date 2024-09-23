def test(var0):
    str_num = str(var0)
    decimal_idx = str_num.find('.')
    if decimal_idx == -1:
        decimal_part = ""
        integer_part = str_num
    else:
        integer_part = str_num[:decimal_idx]
        decimal_part = str_num[decimal_idx:]

    groups = []
    while integer_part:
        groups.insert(0, integer_part[-3:])
        integer_part = integer_part[:-3]

    formatted_str = " ".join(groups) + decimal_part.replace('.', ',')
    return formatted_str

