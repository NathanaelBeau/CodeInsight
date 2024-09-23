def test (var1):

  if var1 > 1:
    for i in range(2, var1//2 + 1):
       if var1 % i == 0:
           return False
 
  return True