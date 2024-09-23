def test(var1):
      for item,value in var1.items():
         var1[item] = list(sorted(value))        
      return var1
