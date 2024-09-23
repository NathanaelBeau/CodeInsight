def test(str0):
    midlen = len(str0) // 2
    newstr = str0[:midlen] + str0[midlen+1:]
    return newstr
