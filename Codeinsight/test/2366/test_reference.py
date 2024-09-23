def test(str0: str, var0: int, var1: int, str1: str, str2: str) -> str:
    slist = list(str0)
    for i, c in enumerate(slist):
        if slist[i] == str1 and var0 <= i <= var1:
            slist[i] = str2
    return ''.join(slist)
