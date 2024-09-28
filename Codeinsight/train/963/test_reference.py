def test(str0):
    result = ""
    escape = False

    for char in str0:
        if char == "\\":
            if escape:
                result += char
                escape = False
            else:
                escape = True
        else:
            result += char
            escape = False

    return result
