def test(str0):
    if not str0:
        return str0
    if str0[0].isupper():
        return str0[0].lower() + str0[1:]
    else:
        return str0[0].upper() + str0[1:]