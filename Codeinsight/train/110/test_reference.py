def test(var1):
    num_seq = [var1]
    if var1 < 1:
       return []
    while var1 > 1:
       if var1 % 2 == 0:
         var1 = var1 / 2
       else:
         var1 = 3 * var1 + 1
       num_seq.append(var1)    
    return num_seq
