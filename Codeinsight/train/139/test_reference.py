def test(dict1, var1):
    if var1 in dict1:
         dict1.pop(var1)
         return dict1
    else:
         return dict1
