def test(lst1):
     fst   = lst1[0]
     last  = lst1[-1]
     lst1[0]  = last
     lst1[-1] = fst  
     return lst1