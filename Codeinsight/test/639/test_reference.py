def test(str0):
    int_part = ""
    for char in str0:
        if char == '.':
            break
        int_part += char
    return int(int_part)

