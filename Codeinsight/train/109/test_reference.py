def test(var1, var2):
    list_str1 = list(var1)
    list_str1.sort()
    list_str2 = list(var2)
    list_str2.sort()

    return (list_str1 == list_str2)
