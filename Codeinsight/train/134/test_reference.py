def test(dict1, var1):
    if var1 in dict1: 
        del dict1[var1]
        return dict1
    else:
        return dict1
