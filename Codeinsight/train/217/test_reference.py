def test(var1):
     m    = max( ord(c) for c in var1)
     argm = var1.index(chr(m))
     return var1[argm]
