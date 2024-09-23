def test(var0):
    result = []
    for char in var0:
        if ord(char) > 127:
            result.append("\\u{:04x}".format(ord(char)))
        else:
            result.append(char)
    return ''.join(result)
