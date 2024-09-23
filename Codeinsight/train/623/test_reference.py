def test(str0):
    if str0 == '':
        return str0
    else:
        return test(str0[1:]) + str0[0]

