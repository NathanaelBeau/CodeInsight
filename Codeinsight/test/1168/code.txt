def test(str0):
    for char in set(str0):
        if str0.count(char) >= 3:
            str0 = str0.replace(char, '')
    return str0
