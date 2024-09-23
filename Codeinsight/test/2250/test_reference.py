def test(str0, var0, var1):
    slist = list(str0)
    for i, c in enumerate(slist):
        if slist[i] == ';' and var0 <= i <= var1:
            slist[i] = ':'
    return ''.join(slist)
