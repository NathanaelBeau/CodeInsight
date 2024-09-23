def test(str0):
    slist = list(str0)
    for i, c in enumerate(slist):
        if slist[i] == ';' and 0 <= i <= 3:
            slist[i] = ':'
    return ''.join(slist)
