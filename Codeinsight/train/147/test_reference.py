def test(var1,var2):
      tokens = var2.split()
      c      = 0
      for tok in tokens:
           if tok == var1:
               c += 1
      return c
