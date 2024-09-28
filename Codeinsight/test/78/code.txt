def test(str0):
    decoded_str = str0.decode("utf-8")
    char_list = []
    for character in decoded_str:
        char_list.append(character)
    return char_list
