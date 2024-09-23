def test(str0):
    result = ""
    for char in str0:
        if char == '\u200b':
            result += '*'
        else:
            result += char
    return result
