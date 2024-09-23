def test(str0):
    result = ""
    for char in str0:
        if not char.isdigit():
            result += char
    return result

