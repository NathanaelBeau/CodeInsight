def test(str0):
    hex_chars = "0123456789ABCDEF"
    str0 = str0.upper()
    hex_num = 0
    for char in str0:
        if char not in hex_chars:
            return None
        hex_num = hex_num * 16 + hex_chars.index(char)
    return hex_num
